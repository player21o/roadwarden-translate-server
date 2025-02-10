import { db } from "../../app/db/db";
import { dictTable, UserPermission, usersTable } from "../../app/db/schema";

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
