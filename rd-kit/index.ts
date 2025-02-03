import "dotenv/config";
import { exec } from "child_process";
import { db } from "../app/db/db";
import { existsSync, mkdirSync } from "fs";
import { convertArgs } from "./types";

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
    console.log(log);
    if (log) console.log("making a backup...");

    if (!existsSync(import.meta.dirname + "/backups"))
      mkdirSync(import.meta.dirname + "/backups");

    exec(
      `pg_dump -d ${db_url} > ${import.meta.dirname}/backups/${new Date()
        .toLocaleString("ru-RU")
        .replaceAll(".", "-")
        .replaceAll(", ", "_")
        .replaceAll(":", "-")}.sql`
    );
  },
  parse: (backup = true) => {
    if (backup) fcs.backup();
  },
};

function isFcsCommand(command: string): command is keyof typeof fcs {
  return command in fcs;
}

if (process.argv[2] !== undefined) {
  const command = process.argv[2];
  if (isFcsCommand(command)) {
    console.log(
      convertArgs(fcs[command], process.argv.slice(3, process.argv.length))
    );
    fcs[command](
      ...convertArgs(fcs[command], process.argv.slice(3, process.argv.length))
    );
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
