import "dotenv/config";
import { exec, execSync } from "child_process";
import { db } from "../app/db/db";
import * as fs from "fs";
import { existsSync, mkdirSync, readFileSync } from "fs";
import { parse } from "./utils/parse";
import { cardsTable, Files } from "../app/db/schema";

type ConverterMap = {
  boolean: (input: string) => boolean;
  number: (input: string) => number;
  string: (input: string) => string;
};

const converterMap: ConverterMap = {
  boolean: (input) => input.toLowerCase() === "true",
  number: (input) => Number(input),
  string: (input) => input,
};

export const db_url = process.env.DATABASE_URL!;

export const fcs = {
  backup: (log: boolean = true) => {
    if (log)
      console.log(
        "making a backup... (you can restore it with 'restore' option)"
      );

    if (!existsSync(import.meta.dirname + "/backups"))
      mkdirSync(import.meta.dirname + "/backups");

    execSync(
      `pg_dump -d ${db_url} > ${import.meta.dirname}/backups/${new Date()
        .toLocaleString("ru-RU")
        .replaceAll(".", "-")
        .replaceAll(", ", "_")
        .replaceAll(":", "-")}.sql`
    );
  },
  parse: async (file: string | null = null, backup = true) => {
    await fcs.clear(true, backup);

    var cards: ReturnType<typeof parse> = [];

    if (file != null) {
      cards = parse(
        readFileSync(import.meta.dirname + `/../app/orfiles/${file}.rpy`, {
          encoding: "utf-8",
        }),
        Files[file as keyof typeof Files]
      );
    } else {
      const dir = await fs.promises.opendir(
        import.meta.dirname + `/../app/orfiles/`
      );
      for await (const dirent of dir) {
        let name = dirent.name.split(".rpy")[0];

        if (dirent.name.endsWith(".rpy")) {
          cards = cards.concat(
            parse(
              await fs.promises.readFile(
                import.meta.dirname + `/../app/orfiles/${name}.rpy`,
                {
                  encoding: "utf-8",
                }
              ),
              Files[name as keyof typeof Files]
            )
          );
        }
      }
    }

    const divided_cards: (typeof cards)[] = []; //because drizzle orm is stupid, we need to divide cards array into chunks
    //otherwise, we get an error maximum stack exceeded blah blah blah

    while (cards.length > 0) divided_cards.push(cards.splice(0, 5000));

    divided_cards.forEach(async (card_group) => {
      await db.insert(cardsTable).values(card_group);
    });

    process.exit();
  },

  clear: async (log = true, backup = true) => {
    if (backup) fcs.backup();
    if (log) console.log("purging all cards...");
    await db.delete(cardsTable);
  },

  restore: () => {
    console.log("restoring the latest backup...");
  },
};

function isFcsCommand(command: string): command is keyof typeof fcs {
  return command in fcs;
}

if (process.argv[2] !== undefined) {
  const command = process.argv[2];
  if (isFcsCommand(command)) {
    fcs[command](...process.argv.slice(3, process.argv.length));
  } else {
    console.log(
      `unrecognized argument '${command}'. Available commands:\n` +
        Object.keys(fcs).join("\n")
    );
  }
} else {
  console.log(
    "no command specified. available commands:\n" + Object.keys(fcs).join("\n")
  );
}
