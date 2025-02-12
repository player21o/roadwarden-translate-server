import { and, eq, ne } from "drizzle-orm";
import { db } from "../../app/db/db";
import {
  cardsTable,
  dictTable,
  Files,
  portalsTable,
  UserPermission,
  usersTable,
} from "../../app/db/schema";
import { Presets, SingleBar } from "cli-progress";

type JSONUsers = [
  string, //id
  string, //former key
  [
    string, //name
    number, //num. of comments
    [], //idk
    { [key: string]: (number | [number, [number, number, number]])[] }, //translated cards with dates
    string[], //allowed files
    [], //bookmarks
    string, //avatar_url
    [] //roles
  ]
][];

export async function transfer_users(data: JSONUsers) {
  await db.delete(usersTable);

  const insert_data: (typeof usersTable.$inferInsert)[] = data.map(
    ([
      id,
      key,
      [name, commits, _, translated, allowed, __, avatar_url, ___],
    ]) => {
      return {
        id: id,
        avatar_url: avatar_url,
        name: name,
        permissions: allowed.map((a) => [
          UserPermission.file,
          a.split(".rpy")[0],
        ]),
      };
    }
  );

  await db.insert(usersTable).values(insert_data);
}

export async function transfer_dict(
  data: [number, string[], string[], string[], string][]
) {
  await db.delete(dictTable);

  const insert_data: (typeof dictTable.$inferInsert)[] = data.map(
    ([id, or, tr, triggers, context]) => {
      return {
        author: "530057366847356968",
        context: context,
        original: or,
        translation: tr,
      };
    }
  );

  await db.insert(dictTable).values(insert_data);
}

type JSONCard = [
  string,
  string,
  number,
  number,
  boolean,
  boolean,
  string[]?,
  string[]?
];

type JSONCards = {
  [file: string]: {
    cards: JSONCard[];
  };
};

export async function transfer_cards(data: JSONCards) {
  const bar = new SingleBar(
    {
      clearOnComplete: false,
      hideCursor: false,
      format: " {bar} | {filename} | {value}/{total}",
      fps: 60,
    },
    Presets.shades_grey
  );
  bar.start(Object.keys(data).length, 0);

  Object.keys(data).forEach((file_name) => {
    bar.increment(1, { filename: file_name });

    data[file_name]!.cards.forEach(
      async ([or, tr, id, line, hidden, unlinked, or_search, tr_search]) => {
        await db
          .update(cardsTable)
          .set({ translation: tr, search_translation: tr_search })
          .where(
            and(
              eq(
                cardsTable.file,
                Files[file_name.split(".rpy")[0] as keyof typeof Files]
              ),
              eq(cardsTable.original, or)
            )
          );
      }
    );
  });

  bar.stop();

  console.log(
    ((
      await db
        .select()
        .from(cardsTable)
        .where(
          and(ne(cardsTable.translation, ""), eq(cardsTable.hidden, false))
        )
    ).length /
      (await db.select().from(cardsTable).where(eq(cardsTable.hidden, false)))
        .length) *
      100
  );
}

export function transfer_portals(data: JSONCards) {
  const bar = new SingleBar(
    {
      clearOnComplete: false,
      hideCursor: false,
      format: " {bar} | {filename} (portals) | {value}/{total}",
      fps: 60,
    },
    Presets.shades_grey
  );
  bar.start(Object.keys(data).length, 0);

  Object.keys(data).forEach((file_name) => {
    bar.increment(1, { filename: file_name });

    data[file_name]!.cards.forEach(
      async ([or, tr, id, line, hidden, unlinked]) => {
        const ot = or.trim();
        const tt = tr.trim();

        if (tt.length > 0 && ot.split("\n").length == tt.split("\n").length) {
          ot.split("\n").forEach(async (passage, index) => {
            const p = passage.trim();

            if (p.length > 0 && tr.split("\n")[index]!.trim().length > 0) {
              await db
                .update(portalsTable)
                .set({ translation: tr.split("\n")[index] })
                .where(eq(portalsTable.original, p));
            }
          });
        }
      }
    );
  });

  bar.stop();
}

export function transfer_cards_stats(users: JSONUsers, files: JSONCards) {
  const card_ids: Record<string, Record<number, JSONCard>> = {};

  Object.keys(files).forEach((file_name) => {
    card_ids[file_name] = {};

    files[file_name]!.cards.forEach((card) => {
      card_ids[file_name]![card[2]] = card;
    });
  });

  users.forEach(
    ([
      id,
      key,
      [name, commits, _, translated, allowed, __, avatar_url, ___],
    ]) => {
      let date: Date = new Date();

      Object.keys(translated).forEach(async (file_name) => {
        translated[file_name]!.forEach(async (tr) => {
          let card_id: number = 0;

          if (Array.isArray(tr)) {
            date = new Date(Date.UTC(tr[1][0], tr[1][1], tr[1][2], 0, 0, 0));

            card_id = tr[0];
          } else {
            card_id = tr;
          }

          //console.log(id);

          await db
            .update(cardsTable)
            .set({
              first_translated_user_id: id.toString(),
              first_translated_date: date,
            })
            .where(
              and(
                eq(
                  cardsTable.file,
                  Files[file_name.split(".rpy")[0] as keyof typeof Files]
                ),
                eq(cardsTable.original, card_ids[file_name]![card_id]![0])
              )
            );
        });
      });
    }
  );
}
