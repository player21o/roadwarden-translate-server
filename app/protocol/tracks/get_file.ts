import { eq } from "drizzle-orm";
import { db } from "../../db/db";
import { cardsTable, Files } from "../../db/schema";
import { Status } from "../packets";
import { prot } from "../server";
import { readFile } from "node:fs/promises";

export function get_file_listener() {
  prot.listen("get_file", async ({ data: { name }, answer }) => {
    if (Object.keys(Files).includes(name)) {
      const file = Files[name as keyof typeof Files];

      const query = await db
        .select()
        .from(cardsTable)
        .where(eq(cardsTable.file, file));

      answer({
        status: Status.success,
        file: query,
        original_file: await readFile(
          `${import.meta.dirname}/../../orfiles/${name}.rpy`,
          {
            encoding: "utf-8",
          }
        ),
      });
    } else {
      answer({ status: Status.failure });
    }
  });
}
