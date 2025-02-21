import { config } from "../../config";
import { Status, Tracks } from "../packets";
import { prot } from "../server";

export function get_info_listener() {
  prot.listen("get_info", ({ data, answer }) => {
    switch (data.type) {
      case "discord_auth_link":
        answer({ link: config.discord.auth_link, status: 200 });
        break;
      case "translation_stats":
        break;
      default:
        answer({ status: Status.failure });
    }
  });
}
