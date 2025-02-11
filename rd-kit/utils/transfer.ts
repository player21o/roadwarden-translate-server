import { and, eq, like } from "drizzle-orm";
import * as fs from "fs";
import { db } from "../../app/db/db";
import {
  cardsTable,
  dictTable,
  Files,
  UserPermission,
  usersTable,
} from "../../app/db/schema";
import { Presets, SingleBar } from "cli-progress";

export async function transfer_users(
  data: [
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
  ][]
) {
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
        permissions: allowed.map((a) => [UserPermission.file, a]),
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

export async function transfer_cards(data: {
  [file: string]: {
    cards: [string, string, number, number, boolean, boolean][];
  };
}) {
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
      async ([or, tr, id, line, hidden, unlinked]) => {
        await db
          .update(cardsTable)
          .set({ translation: tr })
          .where(
            and(
              eq(
                cardsTable.file,
                Files[file_name.split(".rpy")[0] as keyof typeof Files]
              ),
              like(cardsTable.original, or)
            )
          );
      }
    );
  });

  bar.stop();
}
