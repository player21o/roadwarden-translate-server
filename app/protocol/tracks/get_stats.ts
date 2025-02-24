import { eq, isNotNull } from "drizzle-orm";
import { db } from "../../db/db";
import { cardsTable } from "../../db/schema";
import { Status } from "../packets";
import { prot } from "../server";

export function get_stats_listener() {
  prot.listen("get_stats", async ({ data, answer }) => {
    const start_date = new Date(data.start.toDateString());

    const end_date = new Date(data.end.toDateString());

    /*
    const cards = await db
    .select()
    .from(cardsTable)
    .where(between(cardsTable.first_translated_date, start_date, end_date))
    .orderBy(desc(cardsTable.first_translated_date))
    */

    const dataa: number[] = await Promise.all(
      [
        ...Array(
          Math.floor(
            (start_date.getTime() - end_date.getTime()) / (1000 * 60 * 60 * 24)
          )
        ).keys(),
      ]
        .reverse()
        .map(
          async (d) =>
            (
              await db
                .select()
                .from(cardsTable)
                .where(
                  eq(
                    cardsTable.first_translated_date,
                    new Date(
                      new Date(start_date.valueOf()).setDate(
                        start_date.getDate() - d
                      )
                    )
                  )
                )
            ).length
        )
    );

    answer({
      status: Status.success,
      data: dataa,
    });
  });
}
