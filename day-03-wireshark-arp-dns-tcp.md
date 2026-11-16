# Day 3: Wireshark capture (ARP, DNS, TCP)

## Setup

1. Open Wireshark, double-click the active interface (Wi-Fi or Ethernet).
2. Capture about 5 minutes while browsing or using `curl`, `ping`, `nslookup`.
3. Stop the capture and save it (File -> Save As).

## Display filters

| Protocol | Filter | What to look for |
|---|---|---|
| ARP | `arp` | request "Who has X? Tell Y", reply "X is at MAC" |
| DNS | `dns` | UDP port 53, query then response with the A/AAAA record |
| TCP | `tcp` | SYN, SYN-ACK, ACK, data, FIN |

## ARP

- Resolves an IP address to a MAC address on the local network (layer 2).
- Request is a broadcast (`ff:ff:ff:ff:ff:ff`). Reply is a unicast with the MAC.

## DNS

- Resolves a name to an IP address. Usually UDP port 53.
- Look at the query name, the record type (A, AAAA, MX...), and the answer.
- Useful filters: `dns.qry.name contains "example"`, `dns.flags.response == 1`.

## TCP

- Connection-oriented: starts with the 3-way handshake (see day 4).
- Useful filters: `tcp.port == 80`, `tcp.flags.syn == 1`, `tcp.stream == N`.

## My capture

Fill in from my own capture:

| Protocol | Packet number | Source -> Destination | Info |
|---|---|---|---|
| ARP | | | |
| DNS | | | |
| TCP | | | |
