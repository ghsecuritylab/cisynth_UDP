#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, time

IP = "192.168.0.10"
port = 7777

while True : 
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(b"hey !", (IP, port))
	time.sleep(1)
