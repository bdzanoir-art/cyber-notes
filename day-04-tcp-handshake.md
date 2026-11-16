# Day 4: TCP 3-way handshake and flags

Tool: Wireshark. Command used: `curl http://google.com` (HTTP, port 80).
Filter used to isolate the connection: `tcp.stream == 9`

## Connection

| Role | IP | Port |
|---|---|---|
| Client (my PC) | 10.57.232.25 | 54246 |
| Server (Google) | 172.217.20.238 | 80 |

Result of the request: `301 Moved`, redirect to `www.google.com`.

## 3-way handshake

| # | Packet | Direction | Flags | Seq (rel.) | Ack (rel.) |
|---|---|---|---|---|---|
| 1 | SYN | Client -> Server | SYN | 0 | 0 |
| 2 | SYN-ACK | Server -> Client | SYN, ACK | 0 | 1 |
| 3 | ACK | Client -> Server | ACK | 1 | 1 |

- SYN: the client asks to open a connection and sends its initial sequence number (ISN). Raw ISN = 1128777489.
- SYN-ACK: the server accepts, sends its own ISN, and acknowledges client ISN + 1.
- ACK: the client acknowledges server ISN + 1. The connection is established.
- A SYN uses up one sequence number, so each Ack = the other side's Seq + 1.

## Data exchange

| Packet | Direction | Flags | Seq | Ack | Len | Next Seq |
|---|---|---|---|---|---|---|
| `GET / HTTP/1.1` (Frame 172, stream packet 4) | Client -> Server | PSH, ACK | 1 | 1 | 74 | 75 |
| `HTTP/1.1 301 Moved Permanently` | Server -> Client | PSH, ACK | 1 | 75 | 773 | 774 |

- Next Seq = Seq + Len (1 + 74 = 75; 1 + 773 = 774).
- The server's Ack = 75 confirms the 74 bytes of the GET request.
- The client then acknowledges the reply with Ack = 774.

## Flags

| Flag | Meaning |
|---|---|
| SYN | start a connection, synchronize sequence numbers |
| ACK | acknowledge received data |
| PSH | deliver the data to the application now |
| FIN | close the connection politely |
| RST | reset or refuse a connection |
| URG | urgent data (rare) |

## Wireshark filters

```
tcp.stream == 9
tcp.flags.syn == 1 && tcp.flags.ack == 0     # SYN
tcp.flags.syn == 1 && tcp.flags.ack == 1     # SYN-ACK
tcp.stream == 9 && tcp.flags.fin == 1        # FIN packets
tcp.stream == 9 && tcp.flags.reset == 1      # RST packets
http.host == "google.com"                    # the GET request
```

Raw sequence numbers: Edit -> Preferences -> Protocols -> TCP -> untick "Relative sequence numbers".

## Terminal equivalent (tcpdump)

```
sudo tcpdump -i <interface> -n -S "tcp port 80 and host google.com"
```

Flags appear as `[S]` SYN, `[S.]` SYN-ACK, `[.]` ACK, `[P.]` PSH+ACK, `[F.]` FIN+ACK.
