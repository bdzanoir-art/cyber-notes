# Day 7: Week 1 Review (Networking, TCP/IP)

Quiz score: 7/10

## Mistakes
- TCP = Layer 4 (Transport). IP = Layer 3 (Network).
  - Layer 3 = where the packet goes (IP address, routing).
  - Layer 4 = which program receives it (port, reliability, ordering).
- Usable hosts = 2^(host bits) - 2 (network + broadcast reserved).
  - /24 = 254, /26 = 62, /30 = 2.
- X-Frame-Options: DENY = anti-clickjacking (blocks embedding in an iframe).
  - Vary: Cookie = cache control only, not related to iframes.

## Week 1 summary
- Day 1: OSI vs TCP/IP model
- Day 2: IP addresses, subnets, CIDR
- Day 3: Wireshark capture (ARP, DNS, TCP)
- Day 4: TCP 3-way handshake (SYN, SYN-ACK, ACK)
- Day 5: Django login on loopback is plain HTTP, so the username is readable
- Day 6: Python raw socket HTTP GET, 404 vs 200, path scanner idea, response headers
