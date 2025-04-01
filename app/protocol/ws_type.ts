import { WebSocket } from "ws";
import { db } from "../db/db";
import { usersSessionsTable, usersTable } from "../db/schema";
import { eq } from "drizzle-orm";
import { prot } from "./server";
import { tracks } from "./packets";
import { z } from "zod";

export type UserDBQuery = Required<typeof usersTable.$inferInsert> & {
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

      return query_user;
    } else {
      return null;
    }
  }

  public send(data: Uint8Array) {
    this.ws.send(data);
  }

  public send_packet<T extends keyof typeof tracks>(
    track: T,
    data: z.infer<(typeof tracks)[T]["response"]>
  ) {
    prot.send_full_packet(
      {
        packet: data,
        track_id: track,
        req_id: Math.round(Math.random() * 10000),
      },
      this
    );
  }
}
