import { commit_listener } from "./commit";
import { get_file_listener } from "./get_file";
import { get_info_listener } from "./get_info_listener";
import { get_stats_listener } from "./get_stats";
import { get_usr_listener } from "./get_user";
import { login_listener } from "./login";

export function register_tracks() {
  login_listener();
  get_info_listener();
  get_usr_listener();
  get_stats_listener();
  get_file_listener();
  commit_listener();
}

console.log("up and runnin'");
