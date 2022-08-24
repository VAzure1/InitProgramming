#!/bin/bash/python3

from scapy.all import *

print ("sniffing")

def print_pkt(pkt):
	pkt.show()

pkt = sniff(filter='icmp', prn=print_pkt)