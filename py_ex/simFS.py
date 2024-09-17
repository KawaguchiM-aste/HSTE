# simFS_rect.py
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import datetime
from scipy.io.wavfile import write

# Config.
Fs = 44100
f0 = 
a0 = 1.0
N = 
Tdur = 5.0
Twin = 4/f0

# Prep.
T = 1/f0
w = 
dt = 1/Fs
t = 
a = np.zeros(N+1)
b = np.zeros(N+1)
v = np.arange(1, N+1)
nd = len(t)
x = np.zeros(nd)
now=datetime.datetime.now()
str=now.strftime('%Y%m%d%H%M%S')
exfname = 
t_start = np.random.rand()*(Tdur-Twin) 

# Strict
xt = np.sin(w*t)
xt
xt

# Fourier Series
for i in v:
  a[i]=
  if i%2 == 1:
    b[i]=
  x+= 
x+=a0/2 

# Draw
plt.
plt.
plt.legend()
plt.xlim(t_start, t_start+Twin)
plt.xlabel('Time [s]')
#plt.show()
plt.pause(3)
plt.

# Export to csv&wav
t = t.reshape(nd,1)
x = x.reshape(nd,1)
xt = xt.reshape(nd,1)
df = pd.DataFrame(np.concatenate([t, x], 1))
df.to_csv('{}.csv'.format(exfname), index=False, header=['t','x'])
df = pd.DataFrame(np.concatenate([t, xt], 1))
df.to_csv('{}_strict.csv'.format(exfname), index=False, header=['t','xt'])
print('Fs={}, f0={}, N={}'.format(Fs,f0,N))
print('Exported: {}'.format(exfname))
amp = np.iinfo(np.int16).max
ax = amp*x
axt = amp*xt
write
write('{}_FS.wav'.format(exfname), Fs, ax.astype(np.int16))
# end of file