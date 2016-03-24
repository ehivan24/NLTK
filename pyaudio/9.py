'''
Created on May 25, 2015

@author: edwingsantos
'''

import wave
import struct

from math import sin,pi
N=168 # period
x=range(N) # [0,1,2,...,167]
y=N*[0] # [0,0,0,.....,0]
for i in x:
    y1=4/pi*sin(2*pi*i/N)
    y2=4/(3*pi)*sin(6*pi*i/N)
    y3=4/(5*pi)*sin(10*pi*i/N)
    y[i]=y1+y2+y3
y=1313*y # 1313 periods, y length is now 1313*N



fout = wave.open('sin1313.wav', 'w') # creates a wav file 

fout.setnchannels(1)
fout.setsampwidth(2)
fout.setframerate(44100)
fout.setcomptype('NONE','Not Compressed')

BinStr =""
for i in range(len(y)):
    BinStr = BinStr + struct.pack('h',round(y[i]*20000))
fout.writeframesraw(BinStr)
fout.close()


