# simFS_sawtooth.py
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
import datetime

# Config.
Fs = 44100
f0 = 440
a0 = 1.0
N = 3
Tdur = 3.0
Twin = 4/f0

# Prep.
T = 1/f0
w0 = 2*np.pi*f0
dt = 1/Fs
t = np.arange(dt, Tdur-dt, dt)
a = np.zeros(N+1)
b = np.zeros(N+1)
v = np.arange(1, N+1)
nd = len(t)
x = np.zeros(nd)
t_start = np.random.rand()*(Tdur-Twin) 
now=datetime.datetime.now()
str=now.strftime('%Y%m%d%H%M%S')
exfname = '{}_resFS_sawtooth_{}_{}_{}'.format(str,Fs,f0,N)

# Strict
nT = int(T*Fs)
x = np.cos(w0*t)
n = 1
xt = np.zeros(nd)
for it in range (nd-1):
  if x[it+1]<x[it]:
    xt[it] = -2/T*t[it]+(2*n-1)
  elif x[it+1]>x[it]:
    xt[it] = 2/T*t[it]-(2*n-1)
  if it>1 and it<nd-2:
    if x[it+1]>x[it] and x[it+1]>=x[it+2]:
      n+=1  

# Fourier Series
x = np.zeros(nd)
for i in v:
  if i%2 == 1:
    a[i]=4/(i*np.pi)**2
  x+= a[i]*np.cos(i*w0*t) + b[i]*np.sin(i*w0*t)
x+=a0/2 

# Draw    
plt.plot(t, x, label='Fourier Series', linewidth=3)
plt.plot(t, xt, label='Strict', linewidth=1)
plt.xlim(t_start, t_start+Twin)
plt.legend()
plt.xlabel('Time [s]')
#plt.show()
plt.pause(3)
plt.savefig('{}.svg'.format(exfname))

# Export to wav
t = t.reshape(nd,1)
x = x.reshape(nd,1)
xt = xt.reshape(nd,1)
df = pd.DataFrame(np.concatenate([t, x], 1))
df.to_csv('{}.csv'.format(exfname), index=False, header=['t','x'])
df = pd.DataFrame(np.concatenate([t, xt], 1))
df.to_csv('{}_strict.csv'.format(exfname), index=False, header=['t','xt'])
amp = np.iinfo(np.int16).max
ax = amp*x
axt = amp*xt
write('{}_strict.wav'.format(exfname), Fs, axt.astype(np.int16))
write('{}_FS.wav'.format(exfname), Fs, ax.astype(np.int16))
print('Fs={}, f0={}, N={}'.format(Fs,f0,N))
print('Exported: {}'.format(exfname))
# end of file