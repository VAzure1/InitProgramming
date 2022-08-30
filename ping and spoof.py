#Edit the source ip and destination this is ping program using python and ip spoofing tool
from scapy.all import *
a = IP()
a.src= '10.0.2.4'
a.dst = "8.8.8.8"
b = ICMP()
p = a/b
send(p)
