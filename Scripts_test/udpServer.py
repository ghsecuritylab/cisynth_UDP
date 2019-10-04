#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import numpy as np

IP = "192.168.0.14"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, port))
# ~ UDPbuffer=np.array([])
UDPbuffer=[]
int16perPacket = 5000

while True:
    data, addr = sock.recvfrom(1024)
    for i in range(int16perPacket*2): # each uint16 is sent as 2 uint8
        if i%2 != 0 : UDPbuffer.append(int.from_bytes(data[i:i+2], "big", signed=False))
    print(UDPbuffer, "\n\n")
    UDPbuffer=[]
    # ~ print ("received message:", data)
