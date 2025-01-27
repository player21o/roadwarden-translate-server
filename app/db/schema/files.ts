import { pgTable, text, serial } from "drizzle-orm/pg-core";

const cardSchema = {
  id: serial().primaryKey(),
  translation: text(),
  original: text(),
};

export const mountainroadFile = pgTable("mountainroadrpy", cardSchema);
export const screensFile = pgTable("screensrpy", cardSchema);
export const ruinedvillageFile = pgTable("ruinedvillagerpy", cardSchema);
export const howlersdell2thaismad2File = pgTable(
  "howlersdell2thaismad2rpy",
  cardSchema
);
export const greenmountaintribe1entranceFile = pgTable(
  "greenmountaintribe1entrancerpy",
  cardSchema
);
export const rockslideFile = pgTable("rocksliderpy", cardSchema);
export const fishinghamlet01File = pgTable("fishinghamlet01rpy", cardSchema);
export const creeks01structureFile = pgTable(
  "creeks01structurerpy",
  cardSchema
);
export const dolmenFile = pgTable("dolmenrpy", cardSchema);
export const eudociahouse2specifictopicsFile = pgTable(
  "eudociahouse2specifictopicsrpy",
  cardSchema
);
export const greenmountaintribe2chiefFile = pgTable(
  "greenmountaintribe2chiefrpy",
  cardSchema
);
export const beachFile = pgTable("beachrpy", cardSchema);
export const creeks02elahFile = pgTable("creeks02elahrpy", cardSchema);
export const howlerslairFile = pgTable("howlerslairrpy", cardSchema);
export const beforebeachFile = pgTable("beforebeachrpy", cardSchema);
export const highisland1explorationFile = pgTable(
  "highisland1explorationrpy",
  cardSchema
);
export const howlersdell2thaisFile = pgTable(
  "howlersdell2thaisrpy",
  cardSchema
);
export const howlersdell3othernpcsFile = pgTable(
  "howlersdell3othernpcsrpy",
  cardSchema
);
export const beholderFile = pgTable("beholderrpy", cardSchema);
export const bogentranceFile = pgTable("bogentrancerpy", cardSchema);
export const galerocks03severinaFile = pgTable(
  "galerocks03severinarpy",
  cardSchema
);
export const peltnorth1iasonFile = pgTable("peltnorth1iasonrpy", cardSchema);
export const peltnorth2guardsFile = pgTable("peltnorth2guardsrpy", cardSchema);
export const highisland0prepFile = pgTable("highisland0preprpy", cardSchema);
export const shortcutFile = pgTable("shortcutrpy", cardSchema);
export const stonebridgeFile = pgTable("stonebridgerpy", cardSchema);
export const peltnorth3othernpcsFile = pgTable(
  "peltnorth3othernpcsrpy",
  cardSchema
);
export const watchtowerFile = pgTable("watchtowerrpy", cardSchema);
export const foggylake2foggyFile = pgTable("foggylake2foggyrpy", cardSchema);
export const galerocks04debateFile = pgTable(
  "galerocks04debaterpy",
  cardSchema
);
export const fordFile = pgTable("fordrpy", cardSchema);
export const creeks00firsttimeFile = pgTable(
  "creeks00firsttimerpy",
  cardSchema
);
export const peltnorth0structureFile = pgTable(
  "peltnorth0structurerpy",
  cardSchema
);
export const highisland2returnFile = pgTable(
  "highisland2returnrpy",
  cardSchema
);
export const creeks00roadFile = pgTable("creeks00roadrpy", cardSchema);
export const oldpagosFile = pgTable("oldpagosrpy", cardSchema);
export const prologueFile = pgTable("prologuerpy", cardSchema);
export const ruinedvillagetentFile = pgTable(
  "ruinedvillagetentrpy",
  cardSchema
);
export const fishinghamlet02File = pgTable("fishinghamlet02rpy", cardSchema);
export const foraginggroundFile = pgTable("foraginggroundrpy", cardSchema);
export const nvlchoicesFile = pgTable("nvlchoicesrpy", cardSchema);
export const fallentreeFile = pgTable("fallentreerpy", cardSchema);
export const bogroadFile = pgTable("bogroadrpy", cardSchema);
export const ghoulcaveFile = pgTable("ghoulcaverpy", cardSchema);
export const whitemarshes03orentiusFile = pgTable(
  "whitemarshes03orentiusrpy",
  cardSchema
);
export const foggylake1structureFile = pgTable(
  "foggylake1structurerpy",
  cardSchema
);
export const stonesignFile = pgTable("stonesignrpy", cardSchema);
export const epilogueFile = pgTable("epiloguerpy", cardSchema);
export const howlersdell1structureFile = pgTable(
  "howlersdell1structurerpy",
  cardSchema
);
export const galerocks02npcsFile = pgTable("galerocks02npcsrpy", cardSchema);
export const westgateFile = pgTable("westgaterpy", cardSchema);
export const travelingFile = pgTable("travelingrpy", cardSchema);
export const charactersheetFile = pgTable("charactersheetrpy", cardSchema);
export const ruinedshelterFile = pgTable("ruinedshelterrpy", cardSchema);
export const northernroadFile = pgTable("northernroadrpy", cardSchema);
export const creeks04othernpcsFile = pgTable(
  "creeks04othernpcsrpy",
  cardSchema
);
export const druidcave1File = pgTable("druidcave1rpy", cardSchema);
export const banditshideout1structureFile = pgTable(
  "banditshideout1structurerpy",
  cardSchema
);
export const whitemarshes02helviusFile = pgTable(
  "whitemarshes02helviusrpy",
  cardSchema
);
export const mapFile = pgTable("maprpy", cardSchema);
export const howlersdell4confrontationFile = pgTable(
  "howlersdell4confrontationrpy",
  cardSchema
);
export const invFile = pgTable("invrpy", cardSchema);
export const oldtunnel2File = pgTable("oldtunnel2rpy", cardSchema);
export const galerocks01structureFile = pgTable(
  "galerocks01structurerpy",
  cardSchema
);
export const eudociahouse1structureFile = pgTable(
  "eudociahouse1structurerpy",
  cardSchema
);
export const foggylake3othernpcsFile = pgTable(
  "foggylake3othernpcsrpy",
  cardSchema
);
export const eudociahouse3invitationFile = pgTable(
  "eudociahouse3invitationrpy",
  cardSchema
);
export const huntercabinFile = pgTable("huntercabinrpy", cardSchema);
export const oldtunnel1File = pgTable("oldtunnel1rpy", cardSchema);
export const sleepingFile = pgTable("sleepingrpy", cardSchema);
export const creeks03efrenFile = pgTable("creeks03efrenrpy", cardSchema);
export const peltnorth4tuliaFile = pgTable("peltnorth4tuliarpy", cardSchema);
export const peatfieldFile = pgTable("peatfieldrpy", cardSchema);
export const westerncrossroadsFile = pgTable(
  "westerncrossroadsrpy",
  cardSchema
);
export const largeencountersFile = pgTable("largeencountersrpy", cardSchema);
export const shopFile = pgTable("shoprpy", cardSchema);
export const monasteryFile = pgTable("monasteryrpy", cardSchema);
export const banditshideout2glauciaFile = pgTable(
  "banditshideout2glauciarpy",
  cardSchema
);
export const journal_glossary_endscreenFile = pgTable(
  "journal_glossary_endscreenrpy",
  cardSchema
);
export const druidcave2insideFile = pgTable("druidcave2insiderpy", cardSchema);
export const whitemarshes01structureFile = pgTable(
  "whitemarshes01structurerpy",
  cardSchema
);
export const epilogue_altFile = pgTable("epilogue_altrpy", cardSchema);
export const restFile = pgTable("restrpy", cardSchema);
export const giantstatueFile = pgTable("giantstatuerpy", cardSchema);
export const militarycampregularFile = pgTable(
  "militarycampregularrpy",
  cardSchema
);
export const wandererFile = pgTable("wandererrpy", cardSchema);
export const vinesFile = pgTable("vinesrpy", cardSchema);
export const southerncrossroadsFile = pgTable(
  "southerncrossroadsrpy",
  cardSchema
);
export const fileSchemas = {
  "mountainroad.rpy": mountainroadFile,
  "screens.rpy": screensFile,
  "ruinedvillage.rpy": ruinedvillageFile,
  "howlersdell2thaismad2.rpy": howlersdell2thaismad2File,
  "greenmountaintribe1entrance.rpy": greenmountaintribe1entranceFile,
  "rockslide.rpy": rockslideFile,
  "fishinghamlet01.rpy": fishinghamlet01File,
  "creeks01structure.rpy": creeks01structureFile,
  "dolmen.rpy": dolmenFile,
  "eudociahouse2specifictopics.rpy": eudociahouse2specifictopicsFile,
  "greenmountaintribe2chief.rpy": greenmountaintribe2chiefFile,
  "beach.rpy": beachFile,
  "creeks02elah.rpy": creeks02elahFile,
  "howlerslair.rpy": howlerslairFile,
  "beforebeach.rpy": beforebeachFile,
  "highisland1exploration.rpy": highisland1explorationFile,
  "howlersdell2thais.rpy": howlersdell2thaisFile,
  "howlersdell3othernpcs.rpy": howlersdell3othernpcsFile,
  "beholder.rpy": beholderFile,
  "bogentrance.rpy": bogentranceFile,
  "galerocks03severina.rpy": galerocks03severinaFile,
  "peltnorth1iason.rpy": peltnorth1iasonFile,
  "peltnorth2guards.rpy": peltnorth2guardsFile,
  "highisland0prep.rpy": highisland0prepFile,
  "shortcut.rpy": shortcutFile,
  "stonebridge.rpy": stonebridgeFile,
  "peltnorth3othernpcs.rpy": peltnorth3othernpcsFile,
  "watchtower.rpy": watchtowerFile,
  "foggylake2foggy.rpy": foggylake2foggyFile,
  "galerocks04debate.rpy": galerocks04debateFile,
  "ford.rpy": fordFile,
  "creeks00firsttime.rpy": creeks00firsttimeFile,
  "peltnorth0structure.rpy": peltnorth0structureFile,
  "highisland2return.rpy": highisland2returnFile,
  "creeks00road.rpy": creeks00roadFile,
  "oldpagos.rpy": oldpagosFile,
  "prologue.rpy": prologueFile,
  "ruinedvillagetent.rpy": ruinedvillagetentFile,
  "fishinghamlet02.rpy": fishinghamlet02File,
  "foragingground.rpy": foraginggroundFile,
  "nvlchoices.rpy": nvlchoicesFile,
  "fallentree.rpy": fallentreeFile,
  "bogroad.rpy": bogroadFile,
  "ghoulcave.rpy": ghoulcaveFile,
  "whitemarshes03orentius.rpy": whitemarshes03orentiusFile,
  "foggylake1structure.rpy": foggylake1structureFile,
  "stonesign.rpy": stonesignFile,
  "epilogue.rpy": epilogueFile,
  "howlersdell1structure.rpy": howlersdell1structureFile,
  "galerocks02npcs.rpy": galerocks02npcsFile,
  "westgate.rpy": westgateFile,
  "traveling.rpy": travelingFile,
  "charactersheet.rpy": charactersheetFile,
  "ruinedshelter.rpy": ruinedshelterFile,
  "northernroad.rpy": northernroadFile,
  "creeks04othernpcs.rpy": creeks04othernpcsFile,
  "druidcave1.rpy": druidcave1File,
  "banditshideout1structure.rpy": banditshideout1structureFile,
  "whitemarshes02helvius.rpy": whitemarshes02helviusFile,
  "map.rpy": mapFile,
  "howlersdell4confrontation.rpy": howlersdell4confrontationFile,
  "inv.rpy": invFile,
  "oldtunnel2.rpy": oldtunnel2File,
  "galerocks01structure.rpy": galerocks01structureFile,
  "eudociahouse1structure.rpy": eudociahouse1structureFile,
  "foggylake3othernpcs.rpy": foggylake3othernpcsFile,
  "eudociahouse3invitation.rpy": eudociahouse3invitationFile,
  "huntercabin.rpy": huntercabinFile,
  "oldtunnel1.rpy": oldtunnel1File,
  "sleeping.rpy": sleepingFile,
  "creeks03efren.rpy": creeks03efrenFile,
  "peltnorth4tulia.rpy": peltnorth4tuliaFile,
  "peatfield.rpy": peatfieldFile,
  "westerncrossroads.rpy": westerncrossroadsFile,
  "largeencounters.rpy": largeencountersFile,
  "shop.rpy": shopFile,
  "monastery.rpy": monasteryFile,
  "banditshideout2glaucia.rpy": banditshideout2glauciaFile,
  "journal_glossary_endscreen.rpy": journal_glossary_endscreenFile,
  "druidcave2inside.rpy": druidcave2insideFile,
  "whitemarshes01structure.rpy": whitemarshes01structureFile,
  "epilogue_alt.rpy": epilogue_altFile,
  "rest.rpy": restFile,
  "giantstatue.rpy": giantstatueFile,
  "militarycampregular.rpy": militarycampregularFile,
  "wanderer.rpy": wandererFile,
  "vines.rpy": vinesFile,
  "southerncrossroads.rpy": southerncrossroadsFile,
} as const;
