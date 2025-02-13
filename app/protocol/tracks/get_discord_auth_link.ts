import { config } from "../../config";
import { Tracks } from "../packets";
import { prot } from "../server";

export function discord_auth_link_listener() {
  prot.listen(Tracks.discordlink, (packet) => {
    packet.answer({ url: config.discord.auth_link });
  });
}
