import { WebSocket } from "ws";
import { db } from "../db/db";
import { usersSessionsTable, usersTable } from "../db/schema";
import { eq } from "drizzle-orm";

export type UserDBQuery = typeof usersTable.$inferInsert & {
  sessions: (typeof usersSessionsTable.$inferInsert)[];
};

export class WsType {
  private ws: WebSocket;

  public ip: string;
  public user_id: string | null = null;

  constructor(ws: WebSocket, ip: string) {
    this.ws = ws;
    this.ip = ip;
  }

  public get user() {
    if (this.user_id !== null) {
      return db
        .select()
        .from(usersTable)
        .where(eq(usersTable.id, this.user_id))
        .leftJoin(
          usersSessionsTable,
          eq(usersSessionsTable.user_id, usersTable.id)
        )
        .orderBy(usersTable.id);
    } else {
      return null;
    }
  }

  public async getUser() {
    if (this.user_id !== null) {
      const result = await db
        .select()
        .from(usersTable)
        .innerJoin(
          usersSessionsTable,
          eq(usersTable.id, usersSessionsTable.user_id)
        );

      const query_user = result[0]!.users;
      const query: UserDBQuery = { ...query_user, sessions: [] };

      result.forEach(({ users, users_sessions }) => {
        query.sessions.push(users_sessions);
      });

      return query;
    } else {
      return null;
    }
  }

  public send(data: Uint8Array) {
    this.ws.send(data);
  }
}
