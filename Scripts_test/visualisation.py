#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading, time
import numpy as np
import matplotlib.pyplot as plt

IP = "192.168.0.14"
# ~ port = 7777
port = 2039
visualisationBuffer = np.array([]*500)

def UDPlistener(bufferSize):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, port))
    while True:
        data, addr = sock.recvfrom(bufferSize)
        UDPbuffer = np.asarray(data)
        updateVisualisation()
        print ("received message:", data)

def updateVisualisation() :
    
    pass
    
def plotData(data):
    fig, ax = plt.subplots(ncols=1)
    ax.imshow(data, interpolation='none')
    ax.add_patch(c)
    plt.show()
    
    

if __name__ == '__main__':
    plt.style.use('grayscale')
    UDPthread = threading.Thread(target = UDPlistener, args=(1024))
    UDPthread.start()
    while True : 
         try : 
             plotData(np.random.random(size=(20, 20)))
             time.sleep(.1)
         except KeyboardInterrupt :
             UDPthread.stop()
             raise SystemExit
