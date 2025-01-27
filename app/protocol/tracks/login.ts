import { prot } from "../server";
import { Status, Tracks } from "../packets";
import { usersSessionsTable, usersTable } from "../../db/schema/schema";
import { UserDBQuery, WsType } from "../ws_type";
import { db } from "../../main";
import { eq } from "drizzle-orm";
import fetch from "node-fetch";

prot.listen(
  Tracks.login,
  async (packet, ws) => {
    const user = await ws.getUser();

    if (user != null) {
      packet.answer!({ status: Status.failure }); //user is logged in, but we need user logged out
    } else {
      if (packet.method == "session" && packet.token != undefined) {
        //if user logs with a session
        packet.answer!({
          status: await login_through_session(packet.token, ws),
        });
      }
    }
  },
  10
);

const get_session = async (token: string) => {
  return db
    .select()
    .from(usersSessionsTable)
    .where(eq(usersSessionsTable.token, token));
};

async function login_user(ws: WsType, user_id: number) {
  ws.user_id = user_id;
}

async function prolong_session(token: string) {
  await db
    .update(usersSessionsTable)
    .set({ expires: new Date(new Date().getTime() + 86400000 * 7) }) //session lives 7 days
    .where(eq(usersSessionsTable.token, token));
}

async function login_through_session(
  token: string,
  ws: WsType
): Promise<Status> {
  const query = await get_session(token);

  if (query[0] != undefined) {
    //if session exists
    const session = query[0];

    if (session.ip == ws.ip) {
      //for additional security
      if (new Date() > session.expires) {
        //if session has been expired, DELETE it
        await db
          .delete(usersSessionsTable)
          .where(eq(usersSessionsTable.token, token));
      } else {
        //if it is not...
        await prolong_session(token);

        login_user(ws, session.user_id);

        return Status.success;
      }
    }
  }

  return Status.failure;
}

async function login_through_discord(token: string, ws: WsType) {}
