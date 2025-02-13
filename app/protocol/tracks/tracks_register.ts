import { discord_auth_link_listener } from "./get_discord_auth_link";
import { login_listener } from "./login";

export function register_tracks() {
  login_listener();
  discord_auth_link_listener();
}

console.log("up and runnin'");
