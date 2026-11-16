# Day 2: IP addresses, subnets, CIDR

## IPv4 basics

- 32 bits, written as 4 octets (0-255), e.g. `192.168.1.10`.
- An address has a network part and a host part. The subnet mask (or CIDR prefix) says where the split is.
- `/24` means the first 24 bits are the network: mask `255.255.255.0`.

## Special ranges

| Range | Use |
|---|---|
| 10.0.0.0/8 | private |
| 172.16.0.0/12 (172.16.0.0 - 172.31.255.255) | private |
| 192.168.0.0/16 | private |
| 127.0.0.0/8 | loopback (localhost) |
| 169.254.0.0/16 | APIPA (no DHCP answer) |

## CIDR table

| Prefix | Mask | Block size | Usable hosts |
|---|---|---|---|
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

Formula: usable hosts = 2^(32 - prefix) - 2 (minus the network and broadcast addresses).

## Method to find network and broadcast

1. Find the octet where the mask is not 255 or 0. Block size = 256 - mask value in that octet.
2. Network address = the largest multiple of the block size that is <= the address value in that octet.
3. Broadcast = network + block size - 1 (in that octet). Usable range = network + 1 to broadcast - 1.

Example: `192.168.10.77/26`: block 64, network `192.168.10.64`, broadcast `192.168.10.127`, hosts `.65` to `.126`.

## Practice problems (with answers)

| # | Address | Network | Broadcast | Usable hosts |
|---|---|---|---|---|
| 1 | 10.0.0.5/8 | 10.0.0.0 | 10.255.255.255 | 16,777,214 |
| 2 | 172.16.45.9/20 | 172.16.32.0 | 172.16.47.255 | 4,094 |
| 3 | 192.168.1.130/25 | 192.168.1.128 | 192.168.1.255 | 126 |
| 4 | 192.168.5.200/27 | 192.168.5.192 | 192.168.5.223 | 30 |
| 5 | 192.168.0.9/30 | 192.168.0.8 | 192.168.0.11 | 2 |

## My own 10 problems

Add my solved subnetting problems here.
