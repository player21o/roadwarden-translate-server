import { WebSocket, WebSocketServer } from "ws";
import { Protocol } from "./protocol";
import { WsType } from "./ws_type";

class ServerProtocol extends Protocol {
  private wss = new WebSocketServer({ port: 3000 });
  public clients: WsType[] = [];

  public constructor() {
    super();

    const interval = setInterval(() => {
      (this.wss.clients as Set<WebSocket & { is_alive: boolean }>).forEach(
        function each(ws) {
          if (ws.is_alive === false) return ws.terminate();

          ws.is_alive = false;
          ws.ping();
        }
      );
    }, 30000);

    this.wss.on(
      "connection",
      (ws: WebSocket & { is_alive: boolean }, request) => {
        ws.is_alive = true;
        const socket = new WsType(ws, request.socket.remoteAddress!); //req.headers['x-forwarded-for'].split(',')[0].trim();
        console.log(socket.ip);

        this.clients.push(socket);

        ws.on("message", (raw_data) => {
          this.receive_packet(raw_data as Uint8Array, socket);
        });

        ws.on("close", () => {
          this.clients.splice(this.clients.indexOf(socket));
        });

        ws.on("pong", () => {
          ws.is_alive = true;
        });
      }
    );
  }
}

export let prot = new ServerProtocol();
