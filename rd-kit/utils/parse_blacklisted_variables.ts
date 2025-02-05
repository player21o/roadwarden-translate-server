//tool for parsing variables that don't get displayed to the player
//used in parse.ts
//NOT MEANT TO BE USED

import * as fs from "fs";

function escapeRegExp(string: string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string
}

function removePythonComments(code: string): string {
  // i dont even know what the fuck it is
  // author of this regex pattern: deepseek
  const pattern =
    /(?:'''[\s\S]*?'''|"""[\s\S]*?"""|'[^'\\]*(?:\\.[^'\\]*)*'|"[^"\\]*(?:\\.[^"\\]*)*")|(\s*#.*$)/gm;

  return code.replace(pattern, (match, commentGroup) => {
    return commentGroup !== undefined ? "" : match;
  });
}

const contents: [string, string][] = [];
const strings: string[] = [];
const vars: Set<string> = new Set();
const blacklist: string[] = [];

for await (const file of fs.opendirSync(
  import.meta.dirname + `/../../app/orfiles/`
)) {
  if (file.name.endsWith(".rpy")) {
    contents.push([
      removePythonComments(
        fs.readFileSync(
          import.meta.dirname + `/../../app/orfiles/` + file.name,
          {
            encoding: "utf-8",
          }
        )
      ),
      file.name,
    ]);
  }
}

contents.forEach(([content], index, arr) => {
  let lines: string[] = [];

  content.split("\n").forEach((line) => {
    if (line.search("search") == -1) {
      lines.push(line);
    }
  });

  arr[index]![0] = lines.join("\n");
});

contents.forEach(([content, file]) => {
  let menus = content
    .split("'")
    .map((e) => e.trim())
    .filter((string, index) => index % 2 != 0);

  if (content.search("textbutton \\_\\(") != -1) {
    menus = menus.concat(
      content
        .split('textbutton _("')
        //.filter((string, index) => index % 2 != 0)
        .map((e) => e.split('"')[0]!)
    );
  }

  /*

  if (content.search("textbutton '") != -1) {
    menus = menus.concat(
      content
        .split("textbutton '")
        //.filter((string, index) => index % 2 != 0)
        .map((e) => e.split("'")[0]!)
    );
  }
    */

  if (content.search('text "') != -1) {
    menus = menus.concat(
      content
        .split('text "')
        //.filter((string, index) => index % 2 != 0)
        .map((e) => e.split('"')[0]!)
    );
  }

  if (content.search('text \\_\\("') != -1) {
    menus = menus.concat(
      content
        .split('text _("')
        //.filter((string, index) => index % 2 != 0)
        .map((e) => e.split('"')[0]!)
    );
  }

  if (content.search('tt\\.Action\\("') != -1) {
    menus = menus.concat(
      content
        .split('tt.Action("')
        //.filter((string, index) => index % 2 != 0)
        .map((e) => e.split('"')[0]!)
    );
  }

  menus.map((m) => m.replaceAll("\\n", "\n").replaceAll("\r", "\n"));

  //if (file == "screens.rpy") {
  //  fs.writeFileSync("d.json", JSON.stringify(menus), { encoding: "utf-8" });
  //}

  //console.log(
  //  menus.forEach((menu) => {
  //    console.log(menu.split("'")[1]);
  //  })
  //);

  //console.log(menus.length);
  //console.log("end");
  //console.log(content.split("menu:").length);

  strings.push(...menus);
});

contents.forEach(([content]) => {
  content.split("\n").forEach((line) => {
    //console.log(line.search(/\'/) != -1);
    if (
      line.search(/\$/) != -1 &&
      line.search(/\=/) != -1 &&
      (line.search(/\"/) != -1 || line.search(/\'/) != -1) &&
      line.search(/\./) == -1
    ) {
      //console.log("um");
      vars.add(line.split("$")[1]!.split("=")[0]!.trim());
    }
  });
});

//console.log(
//  strings.forEach((s) => {
//    if (s.search("The gambeson on your arm stops the talons as you") != -1)
//      console.log("yes");
//  })
//);

vars.forEach((v) => {
  let found = false;

  strings.some((string) => {
    //console.log(v);
    //console.log(`/\\[${escapeRegExp(v)}\\]/g`);
    // prettier-ignore
    if (string.search(`${escapeRegExp(v)}`) != -1) {
      //console.log([string, v])
      found = true;
      return true;
    }
  });

  if (!found) {
    blacklist.push(v);
  }
});

//console.log(blacklist);
console.log(JSON.stringify(blacklist));
