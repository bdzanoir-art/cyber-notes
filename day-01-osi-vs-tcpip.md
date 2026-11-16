# Day 1: OSI vs TCP/IP model

## OSI model (7 layers)

| # | Layer | Role | PDU | Examples |
|---|---|---|---|---|
| 7 | Application | services used by programs | data | HTTP, DNS, SMTP, FTP |
| 6 | Presentation | format, encryption, compression | data | TLS (often placed here), JPEG |
| 5 | Session | open, manage, close sessions | data | NetBIOS, RPC |
| 4 | Transport | end-to-end delivery, ports | segment (TCP) / datagram (UDP) | TCP, UDP |
| 3 | Network | logical addressing, routing | packet | IP, ICMP, routers |
| 2 | Data Link | local delivery, MAC addresses | frame | Ethernet, ARP, switches |
| 1 | Physical | bits on the medium | bits | cables, Wi-Fi radio, hubs |

Memory aid (top to bottom): All People Seem To Need Data Processing.

## TCP/IP model (4 layers)

| TCP/IP layer | OSI layers covered | Examples |
|---|---|---|
| Application | 5, 6, 7 | HTTP, DNS, SSH |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP |
| Network Access (Link) | 1, 2 | Ethernet, Wi-Fi, ARP |

## Key differences

- OSI is a reference model (7 layers). TCP/IP is the model the Internet actually uses (4 layers).
- TCP/IP merges Application, Presentation and Session into one layer, and Physical and Data Link into one.
- OSI is used for teaching and troubleshooting ("which layer is broken?").

## Encapsulation

Data goes down the stack, and each layer adds a header:

```
Application data -> + TCP header = segment -> + IP header = packet -> + Ethernet header = frame -> bits
```

## Quick troubleshooting by layer

- Layer 1: cable unplugged, no link light.
- Layer 2: wrong VLAN, MAC problem.
- Layer 3: wrong IP or gateway, `ping` fails.
- Layer 4: port blocked, service not listening.
- Layer 7: application error (HTTP 500, bad DNS record).
