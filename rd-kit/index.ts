import "dotenv/config";
import { exec, execSync } from "child_process";
import { db } from "../app/db/db";
import * as fs from "fs";
import { existsSync, mkdirSync, readFileSync } from "fs";
import { parse, parse_portals } from "./utils/parse";
import { cardsTable, Files, portalsTable } from "../app/db/schema";
import { MultiBar, Presets, SingleBar } from "cli-progress";
import { insert_bulk } from "./utils/utils";
import { transfer_dict, transfer_users } from "./utils/transfer";

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
      `pg_dump -Fc ${db_url} > ${import.meta.dirname}/backups/${new Date()
        .toLocaleString("ru-RU")
        .replaceAll(".", "-")
        .replaceAll(", ", "_")
        .replaceAll(":", "-")}.dump`
    );
  },
  parse: async (file: string | null = null, backup = true) => {
    await fcs.clear(true, backup);

    console.log("parsing...");

    const files_bar = new SingleBar(
      {
        clearOnComplete: false,
        hideCursor: false,
        format: " {bar} | {filename} | {value}/{total}",
        fps: 60,
      },
      Presets.shades_grey
    );

    files_bar.start(file != null ? 1 : Object.keys(Files).length, 0);

    var cards: ReturnType<typeof parse> = [];

    if (file != null) {
      files_bar.update(1, { filename: file });
      cards = parse(
        readFileSync(import.meta.dirname + `/../app/orfiles/${file}.rpy`, {
          encoding: "utf-8",
        }),
        Files[file as keyof typeof Files]
      );
    } else {
      Object.keys(Files).forEach((file) => {
        //console.log(file);
        cards = cards.concat(
          parse(
            readFileSync(import.meta.dirname + `/../app/orfiles/${file}.rpy`, {
              encoding: "utf-8",
            }),
            Files[file as keyof typeof Files]
          )
        );

        files_bar.increment(1, { filename: file });
      });
    }

    await insert_bulk(cardsTable, cards);

    files_bar.stop();

    await insert_bulk(
      portalsTable,
      parse_portals(await db.select().from(cardsTable), true)
    );

    return;

    //process.exit();
  },

  clear: async (log = true, backup = true) => {
    if (backup) fcs.backup();
    if (log) console.log("purging all cards...");
    await db.delete(cardsTable);
    await db.delete(portalsTable);

    execSync(`psql -f "${import.meta.dirname + "/clear.sql"}" "${db_url}"`);
  },

  restore: () => {
    console.log("restoring the latest backup...");

    const files_dates: [string, Date][] = [];

    const f_list = fs.readdirSync(import.meta.dirname + "/backups");

    f_list.forEach(function (file) {
      let stats = fs.statSync(import.meta.dirname + "/backups/" + file);
      files_dates.push([file, stats.mtime]);
    });

    files_dates.sort(function (a, b) {
      // Turn your strings into dates, and then subtract them
      // to get a value that is either negative, positive, or zero.
      return b[1].getTime() - a[1].getTime();
    });

    if (files_dates[0] != undefined) {
      execSync(
        `pg_restore -c -d "${db_url}" "${
          import.meta.dirname + "/backups/" + files_dates[0][0]
        }"`
      );
    } else {
      console.log("no backups found!");
    }
  },

  transfer: async (type: "users" | "dict", path: string) => {
    fcs.backup();

    const content = JSON.parse(
      fs.readFileSync(import.meta.dirname + "/" + path, { encoding: "utf-8" })
    );

    if (type == "users") {
      await transfer_users(content);
    } else if (type == "dict") {
      await transfer_dict(content);
    }
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
