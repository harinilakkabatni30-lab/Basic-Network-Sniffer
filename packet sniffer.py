from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", packet[IP].proto)
        print("Packet Length  :", len(packet))

print("Starting Packet Sniffer...")
sniff(prn=packet_callback, count=20)
