import { PgInsertValue, PgTable } from "drizzle-orm/pg-core";

import { db } from "../../app/db/db";

export function removePythonComments(code: string): string {
  let inSingleLineString: "'" | '"' | null = null;
  let inMultiLineString: "'''" | '"""' | null = null;
  let escapeNext = false;

  return code
    .split("\n")
    .map((line) => {
      let cleaned = "";
      let commentStart = -1;

      for (let i = 0; i < line.length; i++) {
        const char = line[i];

        // Handle string states
        if (!escapeNext && !inMultiLineString) {
          if (char === "\\") {
            escapeNext = true;
          } else if (char === inSingleLineString) {
            inSingleLineString = null;
          } else if (!inSingleLineString) {
            if (char === "#") {
              commentStart = i;
              break;
            }
            if (char === "'" || char === '"') {
              // Check for triple quotes
              if (
                line.slice(i, i + 3) === "'''" ||
                line.slice(i, i + 3) === '"""'
              ) {
                inMultiLineString = line.slice(i, i + 3) as "'''" | '"""';
                i += 2;
                cleaned += line.slice(i - 2, i + 1);
                continue;
              }
              inSingleLineString = char;
            }
          }
        } else if (escapeNext) {
          escapeNext = false;
        }

        // Handle multi-line strings
        if (inMultiLineString) {
          if (
            line.slice(i, i + inMultiLineString.length) === inMultiLineString
          ) {
            inMultiLineString = null;
            i += inMultiLineString!.length - 1;
          }
        }

        cleaned += char;
      }

      // Preserve original line structure
      return commentStart >= 0
        ? cleaned + line.slice(commentStart).replace(/#.*/, "")
        : cleaned;
    })
    .join("\n");
}

export async function insert_bulk<T extends PgTable>(
  table: T,
  items: PgInsertValue<T, false>[]
) {
  await db.insert(table).values(items);
}
