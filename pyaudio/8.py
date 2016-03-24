'''
Created on May 24, 2015

@author: edwingsantos
'''


import wave
import struct
import scipy.io.wavfile as wavfile
from math import sin, pi
import matplotlib.pyplot as plt

N = 168 # period
x = range(N)
y = N *[0]
'''
for i in x:
    y[i] = 4 /pi *sin(2*pi*i/N)
y = 3 * y
x = range(3*N)
plt.plot(x, y)
'''
#plt.show()
    
    
file = 'pysynth_scale.wav'
wrd = wave.open(file, 'rb')

rate, data = wavfile.read(file)
S1String = wrd.readframes(1)
S1 = struct.unpack('h', S1String)
print 'S1 ', S1[0]

print data[0:5]

for i in x:
    y1 = 4 / pi*sin(2*pi*i/N)
    y2 = 4 / (3*pi)*sin(6*pi*i/N)
    y3 = 4 / (5*pi)*sin(10*pi*i/N)
    y[i] = y1+y2+y3
y = 3*y
x = range(3*N) # calculate with 3 frequency components

print len(y)
plt.plot(x,y)
plt.show()
    

