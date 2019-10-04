#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading, time
import numpy as np
import matplotlib.pyplot as plt

IP = "192.168.0.14"
# ~ IP = "localhost"
port = 7777
xResolution, yResolution = 250, 250 # xResolution must be equal to the number of uint16 sent per packet
visualisationBuffer = np.array([[0]*xResolution]*yResolution)
listenToUDP = True

def UDPlistener(bufferSize):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, port))
    while listenToUDP:
        data, addr = sock.recvfrom(bufferSize)
        UDPbuffer = np.array([])
        for i in range(xResolution*2) :
            if i%2 : np.append(UDPbuffer, int.from_bytes(data[i:i+2], "big", signed=False))
        updateBuffer(UDPbuffer)
        # ~ print ("received message:", data)

def updateBuffer(line) :
    global visualisationBuffer
    visualisationBuffer = np.roll(visualisationBuffer, -1, axis=0)
    visualisationBuffer[-1] = line
    
def plotData(ax, data):
    ax.imshow(data, interpolation='none')
    plt.draw()
    plt.pause(0.1)
    

if __name__ == '__main__':
    plt.style.use('grayscale')
    fig, ax = plt.subplots(figsize=(20 , 20))
    ax.axis('off')
    
    UDPthread = threading.Thread(target = UDPlistener, args=(1024,))
    UDPthread.start()
    print("listening to UDP on %s:%i" % (IP, port))
    
    while True : 
         try : 
             updateBuffer(np.random.randint(2**16, size=xResolution))
             plotData(ax,visualisationBuffer)
             time.sleep(.1)
         except KeyboardInterrupt :
             listenToUDP = False
             UDPthread.join()
             raise SystemExit
