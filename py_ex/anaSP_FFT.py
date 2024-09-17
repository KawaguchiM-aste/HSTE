# anaSP_FFT.py
# required file: funcFFT.py
# Usage: python anaSP_FFT.py <csvFileName>
# e.g. : python anaSP_FFT.py file.csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import funcFFT
import sys

fft = funcFFT.funcFFT()

# Load
args = sys.argv
fname = args[1]
print('... Loading {}'.format(args[1]))
dat = pd.read_csv(fname)
#dat = pd.read_excel(fname, sheet_name='raw', header=0)
#dat = pd.read_excel(fname, sheet_name='RRIT', header=0)
#dat = pd.read_excel(fname, header=0)
fname = fname[0:len(fname)-4]
exfname = 'resFFT_{}'.format(fname)
nd = 
Nch = 
dat = 
t = dat[:,0]
x = dat[:,1:Nch]
dt = np.mean(np.diff(t))
Fs = 1/dt
Twin = np.max(t)/10

# Config.
t_start = np.random.rand()*(np.max(t)-Twin) 
it_start = int(t_start*Fs)

for i in range(Nch-1):
  y,f = 
  if i==0:
    nf = y.shape[0]
    Y = np.zeros((nf, Nch))
    Y[:,0]=f
  ind = np.argmax(y[1:])
  f0 = f[ind+1]
  print('ind={}, f[ind]={}'.format(ind,f0))
  Twin = 2/f0
  it_end = it_start+int(Twin*Fs)
  plt.figure(i)
  plt.subplot(4,1,1)
  plt.plot(t,x[:,i],'b')
  plt.plot(t[it_start:it_end],x[it_start:it_end,i],'r')
  plt.subplot(4,1,2)
  plt.plot(t,x[:,i],'r')
  plt.xlim(t_start, t_start+Twin)
  plt.xlabel('Time [s]')
  plt.subplot(4,1,(3,4))
  plt.plot(f,y)
  plt.xscale('log')
  plt.xlabel('Frequency [Hz]')
  plt.pause(2)
  plt.savefig('{}_ch{}.png'.format(exfname,i+1))
  Y[:,i+1]=y

df = pd.DataFrame(Y)
with pd.ExcelWriter('{}.xlsx'.format(exfname)) as writer:
    df