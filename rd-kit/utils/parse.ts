import { MultiBar, Presets, SingleBar } from "cli-progress";
import { cardsTable, Files, portalsTable } from "../../app/db/schema";

export function removePythonComments(code: string): string {
  // i dont even know what the fuck it is
  // author of this regex pattern: deepseek
  const pattern =
    /(?:'''[\s\S]*?'''|"""[\s\S]*?"""|'[^'\\]*(?:\\.[^'\\]*)*'|"[^"\\]*(?:\\.[^"\\]*)*")|(\s*#.*$)/gm;

  return code.replace(pattern, (match, commentGroup) => {
    return commentGroup !== undefined ? "" : match;
  });
}

export function parse(
  content: string,
  file_name: Files
): (typeof cardsTable.$inferInsert)[] {
  function filter(str: string, line: string) {
    const strm = str.trim();

    return (
      strm.length > 0 &&
      str != "nvl" &&
      str.search("==") == -1 &&
      !(str.charAt(0) == "#" && str.search(" ") == -1) &&
      !(str.search(/\./) != -1 && str.search(" ") == -1) &&
      !(strm.charAt(0) == "(" && strm.charAt(strm.length - 1) == ")") &&
      !(strm.search("<") != -1 && strm.search(">") != -1) &&
      !(strm.search("==") != -1 || strm.search("!=") != -1)
    );
  }

  function should_be_hidden(str: string, line: string) {
    const strm = str.trim();

    return strm.search(" ") == -1 && strm.toLowerCase() == str;
  }

  content = removePythonComments(content); //remove any comments

  const cards: (typeof cardsTable.$inferInsert)[] = [];
  const lines = content.split("\n");
  const all_strings: string[] = []; // array for all strings to avoid their duplication

  function addCard(card: typeof cardsTable.$inferInsert, line: string) {
    if (!all_strings.includes(card.original) && filter(card.original, line)) {
      all_strings.push(card.original);
      card.hidden = should_be_hidden(card.original, line);
      card.original = card.original.replaceAll("\\n", "\n");
      cards.push(card);
    }
  }

  var inCard = false;
  var potentialCard = "";
  var cardStartLine = 0;
  var cardEndLine = 0;
  var cardSearchWords: string[] = [];

  lines.forEach((line, index) => {
    const trimmed_line = line.trim();

    if (
      (line.match(/'/g) || []).length > 1 ||
      (line.match(/"/g) || []).length > 1
    ) {
      //check if the string is one-liner

      if (line.search("==") == -1 && line.search("search") == -1) {
        //if there are no search words
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
      } else {
        cardSearchWords = line //add all search words
          .split('"')
          .filter((string, index) => index % 2 != 0);
      }
    } else if (
      (line.match(/'/g) || []).length == 1 ||
      (line.match(/"/g) || []).length == 1
    ) {
      //if the string is located at multiple lines
      if (inCard) {
        const trimmed = line.trim();

        if (trimmed == "'" || trimmed == '"') {
          inCard = false;

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

          potentialCard = "";
        }
      } else {
        inCard = true;
        cardStartLine = index;

        potentialCard +=
          line.search('"') != -1 ? line.split('"')[1] : line.split("'")[1];
      }
    } else if (inCard) {
      potentialCard += line.trimStart();
    }
  });

  return cards;
}

export function parse_portals(cards: ReturnType<typeof parse>, pgs = false) {
  const passages: { original: string; card_id: number }[] = [];
  const marked_passages: number[] = []; //passages that we dont need to process
  const portals: (typeof portalsTable.$inferInsert)[] = []; //actual portals

  cards.forEach((card) => {
    card.original.split("\n").forEach((passage) => {
      const trimmed = passage.trim();

      if (passage.length > 0)
        passages.push({ original: trimmed, card_id: card.id! });
    });
  });

  var progress: SingleBar | null = null;

  if (pgs) {
    //console.log(pgs);
    progress = new SingleBar(
      {
        clearOnComplete: false,
        hideCursor: false,
        format: " {bar} | portals | {value}/{total}",
      },
      Presets.shades_grey
    );
    progress.start(passages.length, 0);
  }

  passages.forEach((first_passage, first_passage_index) => {
    const same_passages: typeof passages = []; //indicates whether the passage is truly unique across the game
    marked_passages.push(first_passage_index);

    passages.forEach((second_passage, second_passage_index) => {
      //we dont wanna compare two identical passages

      if (first_passage.original == second_passage.original) {
        if (first_passage.card_id != second_passage.card_id) {
          same_passages.push(second_passage); //hell yeah!
          marked_passages.push(second_passage_index);
        }
      }
    });

    if (same_passages.length > 0) {
      //if we found any equal passages, create a portal from them
      portals.push({
        original: first_passage.original,
        cards: [first_passage.card_id].concat(
          same_passages.map((e) => e.card_id)
        ),
      });
    }

    if (progress != null) progress.increment(1);
  });

  return portals;
}
