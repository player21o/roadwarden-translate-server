import { cardsTable, Files } from "../../app/db/schema";

export function parse(
  content: string,
  file_name: Files
): (typeof cardsTable.$inferInsert)[] {
  function filter(str: string, line: string) {
    const blacklist = [
      "cairn",
      "shortcut-cairn",
      "music",
      "glaucia",
      "glaucia1",
      "pagan",
      "theunitedchurch",
      "ordersoftruth",
      "fellowship",
      "militarycamp",
      "none",
      "warrior",
      "mage",
      "scholar",
      "ineedmoney",
      "iwantmoney",
      "iwantstatus",
      "iwanttoberemembered",
      "iwanttohelp",
      "iwanttostartanewlife",
      "friendly",
      "playful",
      "distanced",
      "intimidating",
      "vulnerable",
      "tulia",
      "tulia1",
    ];

    const strm = str.trim();

    return (
      strm.length > 0 &&
      str != "nvl" &&
      str.search("==") == -1 &&
      !(str.charAt(0) == "#" && str.search(" ") == -1) &&
      !(str.search(/\./) != -1 && str.search(" ") == -1) &&
      !(strm.charAt(0) == "(" && strm.charAt(strm.length - 1) == ")") &&
      !(strm.search("<") != -1 && strm.search(">") != -1) &&
      line.search("#") == -1 &&
      !blacklist.includes(str)
    );
  }

  function should_be_hidden(str: string, line: string) {
    return false;
  }

  const cards: (typeof cardsTable.$inferInsert)[] = [];
  const lines = content.split("\n");
  const all_strings: string[] = []; // array for all strings to avoid their duplication

  function addCard(card: typeof cardsTable.$inferInsert, line: string) {
    if (
      all_strings.indexOf(card.original) == -1 &&
      filter(card.original, line)
    ) {
      card.hidden = should_be_hidden(card.original, line);
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
        //console.log(string);
        addCard(
          {
            file: file_name,
            line_end: index,
            line_start: index,
            original: string,
            translation: "",
          },
          line
        );
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

          addCard(
            {
              file: file_name,
              line_start: cardStartLine,
              line_end: cardEndLine,
              original: potentialCard,
              translation: "",
            },
            line
          );
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
