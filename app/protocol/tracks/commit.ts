import { eq } from "drizzle-orm";
import { db } from "../../db/db";
import { cardsTable } from "../../db/schema";
import { prot } from "../server";
import { Status, UserPermission } from "../packets";

export function commit_listener() {
  prot.listen("commit", async ({ data: { card_id, content }, answer }, ws) => {
    //ws.send_packet('update', {})

    const user = await ws.getUser();

    if (user != null) {
      const query = await db
        .select()
        .from(cardsTable)
        .where(eq(cardsTable.id, card_id));

      if (query[0] != undefined) {
        const card = query[0];

        if (
          user.permissions.filter(
            (v) =>
              v[0] == UserPermission.file &&
              (v[1] == card.file || v[1] == "all")
          ).length > 0
        ) {
          await translate_card(card_id, content);
          answer({ status: Status.success });
        } else {
          answer({ status: Status.failure });
        }
      } else {
        answer({ status: Status.failure });
      }
    }
  });
}

async function translate_card(id: number, content: string) {
  const query = await db
    .update(cardsTable)
    .set({ translation: content })
    .where(eq(cardsTable.id, id))
    .returning();

  prot.broadcast("update", { type: "card", card: query[0]! });
}
