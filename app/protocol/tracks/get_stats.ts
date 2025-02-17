import { between, desc, eq } from "drizzle-orm";
import { db } from "../../db/db";
import { cardsTable } from "../../db/schema";
import { Tracks } from "../packets";
import { prot } from "../server";

export function get_stats_listener() {
  prot.listen(Tracks.stats, async (packet) => {
    const start_date = new Date(
      packet.start.year,
      packet.start.month,
      packet.start.day
    );

    const end_date = new Date(
      packet.end.year,
      packet.end.month,
      packet.end.day
    );

    console.log(start_date, end_date);

    /*
    const cards = await db
    .select()
    .from(cardsTable)
    .where(between(cardsTable.first_translated_date, start_date, end_date))
    .orderBy(desc(cardsTable.first_translated_date))
    */

    const data: number[] = await Promise.all(
      [
        ...Array(
          Math.floor(
            (start_date.getTime() - end_date.getTime()) / (1000 * 60 * 60 * 24)
          ) + 1
        ).keys(),
      ]
        .reverse()
        .map(async (d) => {
          console.log(
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
            ).length,
            new Date(
              new Date(start_date.valueOf()).setDate(start_date.getDate() - d)
            )
          );
          return (
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
          ).length;
        })
    );

    packet.answer({
      data: data,
    });
  });
}
