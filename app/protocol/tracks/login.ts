import { prot } from "../server";
import { Status } from "../packets";
import { usersSessionsTable, usersTable } from "../../db/schema";
import { WsType } from "../ws_type";
import { db } from "../../db/db";
import { eq } from "drizzle-orm";
import fetch from "node-fetch";
import { config } from "../../config";
import crypto from "crypto";

export function login_listener() {
  prot.listen("login", async ({ data, answer }, ws) => {
    const user = await ws.getUser();

    if (user != null) {
      answer({ status: Status.failure }); //user is logged in, but we need user logged out
    } else {
      if (data.method == "session" && data.token != undefined) {
        //if user logs with a session
        answer(await login_through_session(data.token, ws));
      } else if (data.method == "discord" && data.token != undefined) {
        answer(await login_through_discord(data.token, ws));
      } else {
        answer({ status: Status.failure });
      }
    }
  });
}

function get_session(token: string) {
  //console.log(token);
  return db
    .select()
    .from(usersSessionsTable)
    .where(eq(usersSessionsTable.token, token));
}

function login_user(ws: WsType, user_id: string) {
  ws.user_id = user_id;
}

function get_session_default_date() {
  return new Date(new Date().getTime() + 86400000 * 7);
}

function generate_session_token() {
  return crypto.randomBytes(54).toString("hex");
}

function prolong_session(token: string) {
  return db
    .update(usersSessionsTable)
    .set({ expires: get_session_default_date() }) //session lives 7 days
    .where(eq(usersSessionsTable.token, token));
}

async function login_through_session(
  token: string,
  ws: WsType
): Promise<{ status: Status; user_id?: string }> {
  const query = await get_session(token);

  if (query[0] != undefined) {
    //if session exists
    const session = query[0];
    //console.log("token exists");

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

        return { status: Status.success, user_id: session.user_id };
      }
    }
  }

  return { status: Status.failure };
}

async function create_new_session(
  data: Omit<Omit<typeof usersSessionsTable.$inferInsert, "token">, "expires">
) {
  const token = generate_session_token();

  await db.insert(usersSessionsTable).values({
    ip: data.ip,
    user_id: data.user_id,
    token: token,
    expires: get_session_default_date(),
  });

  return token;
}

function create_new_user(data: typeof usersTable.$inferInsert) {
  return db.insert(usersTable).values(data).returning();
}

async function login_through_discord(
  code: string,
  ws: WsType
): Promise<{ status: Status; session_token?: string; user_id?: string }> {
  //first, we need to obtain *token* for getting the user info to work
  const token_req_body = {
    //client_id: config.discord.client.id,
    //client_secret: config.discord.client.secret,
    grant_type: "authorization_code",
    code: code,
    redirect_uri: config.discord.redirect_url,
  };

  const token_req = await fetch("https://discord.com/api/oauth2/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      Authorization:
        "Basic " +
        btoa(config.discord.client.id + ":" + config.discord.client.secret),
    },
    body: new URLSearchParams(token_req_body),
  });

  //console.log(await token_req.json());

  //console.log(code);

  if (token_req.ok) {
    //console.log("token ok");
    //if there's no problems with code user provided
    const token_req_response = (await token_req.json()) as {
      access_token: string;
    };

    const user_req = await fetch("https://discord.com/api/v10/users/@me", {
      headers: { Authorization: `Bearer ${token_req_response.access_token}` },
    });

    if (user_req.ok) {
      //if there's no problems with accessing user info
      const user_req_response = (await user_req.json()) as {
        id: string;
        username: string;
        avatar: string;
      };

      const get_user = await db
        .select()
        .from(usersTable)
        .where(eq(usersTable.id, user_req_response.id));

      let user_id = "-1";

      if (get_user[0] != undefined) {
        //if user exists
        user_id = get_user[0].id;
      } else {
        //if he doesn't (user is not registered)
        const usr = await create_new_user({
          id: user_req_response.id,
          name: user_req_response.username,
          avatar_url: `https://cdn.discordapp.com/avatars/${user_req_response.id}/${user_req_response.avatar}`, //f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.png'
        });

        user_id = usr[0]!.id;
      }

      const session_token = await create_new_session({
        ip: ws.ip,
        user_id: user_id,
      });

      //login_user(ws, user_id);

      return {
        status: Status.success,
        session_token: session_token,
        user_id: user_id,
      };
    }
  }

  return { status: Status.failure };
}
