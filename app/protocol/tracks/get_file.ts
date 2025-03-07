import { eq } from "drizzle-orm";
import { db } from "../../db/db";
import { cardsTable, Files } from "../../db/schema";
import { Status } from "../packets";
import { prot } from "../server";

export function get_file_listener() {
  prot.listen("get_file", async ({ data: { name }, answer }) => {
    if (Object.keys(Files).includes(name)) {
      const file = Files[name as keyof typeof Files];

      const query = await db
        .select()
        .from(cardsTable)
        .where(eq(cardsTable.file, file));

      answer({ status: Status.success, file: query });
    } else {
      answer({ status: Status.failure });
    }
  });
}
