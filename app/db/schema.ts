import { bigint, boolean, jsonb, pgEnum } from "drizzle-orm/pg-core";
import { timestamp } from "drizzle-orm/pg-core";
import { integer } from "drizzle-orm/pg-core";
import { text } from "drizzle-orm/pg-core";
import { pgTable, serial } from "drizzle-orm/pg-core";

export enum Files {
  mountainroad = "mountainroad",
  screens = "screens",
  ruinedvillage = "ruinedvillage",
  howlersdell2thaismad2 = "howlersdell2thaismad2",
  greenmountaintribe1entrance = "greenmountaintribe1entrance",
  rockslide = "rockslide",
  fishinghamlet01 = "fishinghamlet01",
  creeks01structure = "creeks01structure",
  dolmen = "dolmen",
  eudociahouse2specifictopics = "eudociahouse2specifictopics",
  greenmountaintribe2chief = "greenmountaintribe2chief",
  beach = "beach",
  creeks02elah = "creeks02elah",
  howlerslair = "howlerslair",
  beforebeach = "beforebeach",
  highisland1exploration = "highisland1exploration",
  howlersdell2thais = "howlersdell2thais",
  howlersdell3othernpcs = "howlersdell3othernpcs",
  beholder = "beholder",
  bogentrance = "bogentrance",
  galerocks03severina = "galerocks03severina",
  peltnorth1iason = "peltnorth1iason",
  peltnorth2guards = "peltnorth2guards",
  highisland0prep = "highisland0prep",
  shortcut = "shortcut",
  stonebridge = "stonebridge",
  peltnorth3othernpcs = "peltnorth3othernpcs",
  watchtower = "watchtower",
  foggylake2foggy = "foggylake2foggy",
  galerocks04debate = "galerocks04debate",
  ford = "ford",
  creeks00firsttime = "creeks00firsttime",
  peltnorth0structure = "peltnorth0structure",
  highisland2return = "highisland2return",
  creeks00road = "creeks00road",
  oldpagos = "oldpagos",
  prologue = "prologue",
  ruinedvillagetent = "ruinedvillagetent",
  fishinghamlet02 = "fishinghamlet02",
  foragingground = "foragingground",
  nvlchoices = "nvlchoices",
  fallentree = "fallentree",
  bogroad = "bogroad",
  ghoulcave = "ghoulcave",
  whitemarshes03orentius = "whitemarshes03orentius",
  foggylake1structure = "foggylake1structure",
  stonesign = "stonesign",
  epilogue = "epilogue",
  howlersdell1structure = "howlersdell1structure",
  galerocks02npcs = "galerocks02npcs",
  westgate = "westgate",
  traveling = "traveling",
  charactersheet = "charactersheet",
  ruinedshelter = "ruinedshelter",
  northernroad = "northernroad",
  creeks04othernpcs = "creeks04othernpcs",
  druidcave1 = "druidcave1",
  banditshideout1structure = "banditshideout1structure",
  whitemarshes02helvius = "whitemarshes02helvius",
  map = "map",
  howlersdell4confrontation = "howlersdell4confrontation",
  inv = "inv",
  oldtunnel2 = "oldtunnel2",
  galerocks01structure = "galerocks01structure",
  eudociahouse1structure = "eudociahouse1structure",
  foggylake3othernpcs = "foggylake3othernpcs",
  eudociahouse3invitation = "eudociahouse3invitation",
  huntercabin = "huntercabin",
  oldtunnel1 = "oldtunnel1",
  sleeping = "sleeping",
  creeks03efren = "creeks03efren",
  peltnorth4tulia = "peltnorth4tulia",
  peatfield = "peatfield",
  westerncrossroads = "westerncrossroads",
  largeencounters = "largeencounters",
  shop = "shop",
  monastery = "monastery",
  banditshideout2glaucia = "banditshideout2glaucia",
  journal_glossary_endscreen = "journal_glossary_endscreen",
  druidcave2inside = "druidcave2inside",
  whitemarshes01structure = "whitemarshes01structure",
  epilogue_alt = "epilogue_alt",
  rest = "rest",
  giantstatue = "giantstatue",
  militarycampregular = "militarycampregular",
  wanderer = "wanderer",
  vines = "vines",
  southerncrossroads = "southerncrossroads",
}

export const enum UserPermission {
  file,
  admin,
}

export type UserSession = {
  token: string;
  expires: string; //this is actually a date object but stringified...
  ip: string;
};

export const usersTable = pgTable("users", {
  id: text().primaryKey().notNull(),
  name: text().notNull(),
  avatar_url: text().notNull(),
  permissions: jsonb().notNull().$type<[UserPermission, any?][]>().default([]),
  //sessions: jsonb().$type<UserSession[]>().default([]),
});

export const usersSessionsTable = pgTable("users_sessions", {
  token: text().notNull().primaryKey(),
  user_id: text()
    .references(() => usersTable.id)
    .notNull(),
  expires: timestamp({ mode: "date" }).notNull(),
  ip: text().notNull(),
});

export function enumToPgEnum<T extends Record<string, any>>(
  myEnum: T
): [T[keyof T], ...T[keyof T][]] {
  return Object.values(myEnum).map((value: any) => `${value}`) as any;
}

export const filesEnum = pgEnum("files", enumToPgEnum(Files));

export const cardsTable = pgTable("cards", {
  file: filesEnum().notNull(),
  id: serial().primaryKey().notNull(),
  translation: text().notNull(),
  original: text().notNull(),
  line_start: integer().notNull(),
  line_end: integer().notNull(),
  hidden: boolean().notNull().default(false),
  search_translation: jsonb().notNull().$type<string[]>().default([]),
  search_original: jsonb().notNull().$type<string[]>().default([]),
  first_translated_date: timestamp(),
  first_translated_user_id: text().references(() => usersTable.id),
});

export const dictTable = pgTable("dict", {
  id: serial().primaryKey(),
  original: jsonb().notNull().$type<string[]>().default([]),
  translation: jsonb().notNull().$type<string[]>().default([]),
  context: text().notNull().default(""),
  author: text()
    .references(() => usersTable.id)
    .notNull(),
});

export const portalsTable = pgTable("cards_portals", {
  id: serial().primaryKey().notNull(),
  original: text().notNull(),
  translation: text().notNull().default(""),
  cards: jsonb().notNull().$type<number[]>().default([]),
});
