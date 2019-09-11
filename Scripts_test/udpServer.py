#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP = "192.168.0.14"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, port))

while True:
    data, addr = sock.recvfrom(1024)
    print ("received message:", data)
