import { eq } from "drizzle-orm";
import { db } from "../../db/db";
import { usersTable } from "../../db/schema";
import { Status } from "../packets";
import { prot } from "../server";

export function get_usr_listener() {
  prot.listen("get_user", async ({ data, answer }) => {
    const query = await db
      .select()
      .from(usersTable)
      .where(eq(usersTable.id, data.user_id));

    if (query[0] != undefined) {
      const usr = query[0];

      answer({
        status: Status.success,
        user: {
          id: usr.id,
          name: usr.name,
          avatar_url: usr.avatar_url,
          permissions: usr.permissions,
        },
      });
    } else {
      answer({ status: Status.failure });
    }
  });
}
