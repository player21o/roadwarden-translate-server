import { discord_auth_link_listener } from "./get_discord_auth_link";
import { get_stats_listener } from "./get_stats";
import { get_usr_listener } from "./get_user";
import { login_listener } from "./login";

export function register_tracks() {
  login_listener();
  discord_auth_link_listener();
  get_usr_listener();
  get_stats_listener();
}

console.log("up and runnin'");
