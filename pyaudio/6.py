'''
Created on May 24, 2015

@author: edwingsantos
'''

from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write


from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16
from pylab import plot,show,axis
from matplotlib.mlab import specgram

def plotSpectru(y,Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
 
    plot(frq,abs(Y),'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

Fs = 44100;  # sampling rate

rate,data=read('left3.wav')
y=data[:,1]
lungime=len(y)
timp=len(y)/44100.
t=linspace(0,timp,len(y))

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectru(y,Fs)
show()


show()
