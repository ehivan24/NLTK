'''
Created on May 25, 2015

@author: edwingsantos
'''

#compare two wav files 

import wave, struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile 


file1 = 'left1.wav'
file2 = 'left2.wav'
file3 = 'left5.wav'


musicfile1 = wave.open(file1, 'r')
musicfile2 = wave.open(file2, 'r')
musicfile3 = wave.open(file3, 'r')

frames1 = musicfile1.readframes(256)
frames2 = musicfile2.readframes(256)
frames3 = musicfile3.readframes(256)


frames1 = [struct.unpack('<h', frames1[i]+ frames1[i+1])[0] for i in range(0, len(frames1), 2)]
frames2 = [struct.unpack('<h', frames2[i]+ frames2[i+1])[0] for i in range(0, len(frames2), 2)]
frames3 = [struct.unpack('<h', frames3[i]+ frames3[i+1])[0] for i in range(0, len(frames3), 2)]

plt.plot(frames1, 'r')
plt.plot(frames2, 'g')
plt.plot(frames3, 'b')



#plt.show()

print frames1
print frames2
print frames3




fs1, data1 = wavfile.read(file1)
fs2, data2 = wavfile.read(file2)
fs3, data3 = wavfile.read(file3)

plt.plot(data1, 'r')
plt.plot(data2, 'g')
plt.plot(data3, 'b')
plt.show()

#print data1





