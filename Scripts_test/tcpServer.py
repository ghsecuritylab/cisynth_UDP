#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, time

# ~ host = socket.gethostname()
host = "192.168.0.10"
port = 7777

while True :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.listen(1)
    client, data = s.recv(1024)
    
    time.sleep(1)
    
