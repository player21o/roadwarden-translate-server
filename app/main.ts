import { beachFile, fileSchemas } from "./db/schema/files";
import { FilePacket, Status, Tracks } from "./protocol/packets";
import { prot } from "./protocol/server";
import { db } from "./db/db";

prot.listen(Tracks.user, (packet, ws) => {
  console.log(packet);
  packet.answer!({ status: Status.success });
});

/*



const g: (typeof fileSchemas)["beach.rpy"]["$inferInsert"] = {
  original: "Hello",
  translation: "Привет",
};

const user: typeof schema2.usersTable.$inferInsert = {};

db.query.usersTable.findFirst({ with: { id: 0 } }).then((result) => {
  if (result) {
    if (result.permissions!.indexOf([schema2.UserPermission.file, null])) {
    }
  }
});
*/

const card: typeof beachFile.$inferInsert = {
  original: "Hello",
  translation: "Привет",
};

db.select()
  .from(fileSchemas["beach.rpy"])
  .then((res) => {});

db.insert(fileSchemas["beach.rpy"])
  .values(card)
  .then(() => {
    console.log("new card!");
  });
