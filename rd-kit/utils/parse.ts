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

  function addCard(card: typeof cardsTable.$inferInsert) {
    if (all_strings.indexOf(card.original) == -1 && filter(card.original)) {
      cards.push(card);
      all_strings.push(card.original);
    }
  }

  var inCard = false;
  var potentialCard = "";
  var cardStartLine = 0;
  var cardEndLine = 0;

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
        addCard({
          file: file_name,
          line_end: index,
          line_start: index,
          original: string,
          translation: "",
        });
      });
    } else if (
      (line.match(/'/g) || []).length == 1 ||
      (line.match(/"/g) || []).length == 1
    ) {
      //if the string is located at multiple lines
      if (inCard) {
        const trimmed = line.trimStart();

        if (trimmed == "'" || trimmed == '"') {
          inCard = false;
          potentialCard = "";

          cardEndLine = index;

          addCard({
            file: file_name,
            line_start: cardStartLine,
            line_end: cardEndLine,
            original: potentialCard,
            translation: "",
          });
        }
      } else {
        inCard = true;

        potentialCard +=
          line.search('"') != -1 ? line.split('"')[1] : line.split("'")[1];
      }
    }
  });

  return cards;
}
