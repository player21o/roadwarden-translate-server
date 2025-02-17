import { eq } from "drizzle-orm";
import { db } from "../../db/db";
import { usersTable } from "../../db/schema";
import { Status, Tracks } from "../packets";
import { prot } from "../server";

export function get_usr_listener() {
  prot.listen(Tracks.user, async (packet) => {
    const query = await db
      .select()
      .from(usersTable)
      .where(eq(usersTable.id, packet.id));
    console.log(packet);

    if (query[0] != undefined) {
      const usr = query[0];

      packet.answer({
        status: Status.success,
        id: usr.id,
        name: usr.name,
        avatar_url: usr.avatar_url,
        permissions: usr.permissions,
      });
    } else {
      packet.answer({ status: Status.failure });
    }
  });
}
