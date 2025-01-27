import { relations } from "drizzle-orm";
import { jsonb } from "drizzle-orm/pg-core";
import { timestamp } from "drizzle-orm/pg-core";
import { integer } from "drizzle-orm/pg-core";
import { text } from "drizzle-orm/pg-core";
import { pgTable, serial } from "drizzle-orm/pg-core";

export const enum UserPermission {
  file,
}

export type UserSession = {
  token: string;
  expires: string; //this is actually a date object but stringified...
  ip: string;
};

export const usersTable = pgTable("users", {
  id: serial().primaryKey().notNull(),
  name: text().notNull(),
  avatar_url: text().notNull(),
  permissions: jsonb().notNull().$type<[UserPermission, any?][]>().default([]),
  //sessions: jsonb().$type<UserSession[]>().default([]),
});

export const usersSessionsTable = pgTable("users_sessions", {
  token: text().notNull().primaryKey(),
  user_id: integer()
    .references(() => usersTable.id)
    .notNull(),
  expires: timestamp({ mode: "date" }).notNull(),
  ip: text().notNull(),
});

/*
export const usersSessionsRelation2 = relations(
  usersSessionsTable,
  ({ one }) => ({
    author: one(usersTable, {
      fields: [usersSessionsTable.user_id],
      references: [usersTable.id],
    }),
  })
);
*/
