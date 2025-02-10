import { db } from "../../app/db/db";
import { UserPermission, usersTable } from "../../app/db/schema";

export async function transfer_users(
  data: [
    number, //id
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

  data.forEach(
    async ([
      id,
      key,
      [name, commits, _, translated, allowed, __, avatar_url, ___],
    ]) => {
      await db.insert(usersTable).values({
        id: id.toString(),
        avatar_url: avatar_url,
        name: name,
        permissions: allowed.map((a) => [UserPermission.file, a]),
      });
    }
  );
}
