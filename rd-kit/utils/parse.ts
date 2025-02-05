import { cardsTable, Files } from "../../app/db/schema";

export function parse(
  content: string,
  file_name: Files
): (typeof cardsTable.$inferInsert)[] {
  function filter(str: string, line: string) {
    const blacklisted_vars = [
      "quarters_counter",
      "day_counter_plural",
      "greenmountaintribe_firstattitude",
      "pc_firstvillage",
      "hovlavan_nakedness",
      "creeks_youth_gambling_wager",
      "greenmountaintribe_secondattitude",
      "questsupportofthegreenmountaintribereward",
      "cephasgaiane_shop_select",
      "description_thais_pcopinion",
      "hovlavan_humaninteraction",
      "hovlavan_music",
      "howlerslair_corpse_status",
      "highisland_destination",
      "highisland_lightsource",
      "highisland_spot",
      "pc_futureplans",
      "howlersdell_reputation_status",
      "howlersdell_elpis_about_asterion_help4",
      "severina_firstattitude",
      "iason_stance",
      "iason_about_workforquintus",
      "highisland_crew_dmg_target",
      "foggy_quest_iason_relationship",
      "bestiary_seamonsters_city",
      "ford_side",
      "dalit_firstattitude",
      "tulia_attitude",
      "pyrrhos_firstattitude",
      "whitemarshes_attack_plan",
      "orentius_attitude",
      "sleep_destination",
      "quest_explorepeninsula_result",
      "asterion_found_pcthought",
      "quest_explorepeninsula_mainvillage",
      "endgame_newlife_selected",
      "quintus_attitude",
      "ruinedvillage_arrivingdirection",
      "pc_home_druid",
      "travel_duration_beach",
      "travel_duration_fallentree",
      "travel_duration_eudociahouse",
      "travel_duration_ghoulcave",
      "travel_duration_giantstatue",
      "travel_duration_mountainroad",
      "travel_duration_greenmountaintribe",
      "oldtunnel_exploration_scrap02_trap",
      "oldtunnel_exploration_scrap03_trap",
      "oldtunnel_exploration_scrap05_trap",
      "oldtunnel_exploration_scrap06_trap",
      "oldtunnel_exploration_scrap08_trap",
      "oldtunnel_exploration_scrap11_trap",
      "oldtunnel_exploration_scrap14_trap",
      "oldtunnel_exploration_scrap15_trap",
      "eudocia_image_golem02",
      "eudocia_image_right",
      "eudocia_image_left",
      "eudocia_image_golem01",
      "oldtunnel_magiclight_color",
      "oldtunnel_inside_undead_defeated_burial",
      "sleep_dream_pc_murdered",
      "sleep_dream_pc_battlecounter",
      "asterion_lie",
      "anti_epilogue_village_tulia_fate",
      "anti_epilogue_village_selected",
      "fishinghamlet_harpies_stance",
      "mundanejob_labelname",
      "anti_epilogue_pc_survival_deathcause",
      "sleep_options",
      "wanderer_offering",
      "description_hovlavan04",
    ];

    let found_blacklisted_var = false;

    blacklisted_vars.some((v) => {
      if (line.search("$ " + v) != -1) {
        found_blacklisted_var = true;
        return true;
      }
    });

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
      !found_blacklisted_var
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
      card.original = card.original.replaceAll("\\n", "\n");
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
