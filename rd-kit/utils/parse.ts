import { cardsTable, Files } from "../../app/db/schema";

export function parse(
  content: string,
  file_name: Files
): (typeof cardsTable.$inferInsert)[] {
  function filter(str: string) {
    return str.length > 0;
  }

  const cards: (typeof cardsTable.$inferInsert)[] = [];
  const lines = content.split("\n");
  const all_strings: string[] = []; // array for all strings to avoid their duplication

  var inCard = false;

  lines.forEach((line, index) => {
    const trimmed_line = line.trim();

    if (
      (line.match(/'/g) || []).length > 1 ||
      (line.match(/"/g) || []).length > 1
    ) {
      //check if the string is one-liner
      const strings = line //create an array of strings in that line
        .split('"')
        .filter((string, index) => index % 2 != 0)
        .concat(line.split("'").filter((string, index) => index % 2 != 0));

      strings.forEach((string) => {
        if (all_strings.indexOf(string) == -1 && filter(string)) {
          cards.push({
            file: file_name,
            line_end: index,
            line_start: index,
            original: string,
            translation: "",
          });

          //console.log(string);

          all_strings.push(string);
        }
      });
    }
  });

  return cards;
}
