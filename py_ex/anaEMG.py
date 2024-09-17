# anaEMG.py
# usage: python anaEMG.py <Excel_file>
# e.g. : python exportOpenSignals.py opensignals20XX_EMG

import pandas as pd
import numpy as np
from mat
import sys
from biosppy
from scip

Fc = 5.0  #　ローパスフィルタの遮断周波数

def funcLPF(x, Fc, Fs, order=4):
    Fnq = Fs/2
    nFc = Fc/Fnq
    b,a = 
    y = 
    return y

def func_env(x, Fc, Fs, show=1):
    yh = 
    ay = 
    ayf = f
    t = np.linspace(0, len(x)/Fs, len(x))
    if show == 1:
        plt.plot(t, x, 'k-', linewidth=0.5)
        plt.plot(t, ayf, 'b-', linewidth=1)
        plt.pause(2)
    return ay, ayf

def func_mvc(x, xenv, t, Fs):
    flag = 0
    print('*** calc. MVC ***')
    while flag == 0:
        plt.cla()
        plt.plot
        plt.plot
        plt.pause(2)
        t_start = 
        it_start = int(float(t_start)*Fs)
        t_end = 
        it_end = int(float(t_end)*Fs)
        plt.plot(t[it_start:it_end], xenv[it_start:it_end], 'r-', linewidth=2)
        plt.xlabel('Time [s]')
        plt.pause(2)
        tmp = 
        if tmp.lower() == 'y':
            flag = 1
    rmsEMG = np.sqrt(np.mean(xenv[it_start:it_end]**2))
    plt.plot
    plt.legend()
    plt.pause(3)
    return rmsEMG

if __name__=='__main__':
    args = sys.argv
    fname = args[1]
    print('... Loading {}'.format(fname))
    dat = 
    t = np.array(dat.iloc[:,0])
    x = 

    nd = len(t)
    Fs = 1/np.mean(np.diff(t))
    y = 
    xEMGf = y[1]

    # Envelope
    x_env, 

    # MVC
    plt.figure(2)
    rms_mvc = 
    plt.savefig('{}_mvc.png'.format(fname))
    
    # Prep. Export
    t = t.reshape(nd,1)
    xEMGf = xEMGf.reshape(nd,1)
    x_env_fil = x_env_fil.reshape(nd,1)
    x_env = x_env.reshape(nd,1)

    # Export EMG
    dfEMG = pd.DataFrame(np.concatenate([t, xEMGf, x_env_fil, x_env],1))
    exfname = '{}_fil_tim.xlsx'.format(fname)
    with pd.ExcelWriter(exfname) as writer:
        dfEMG.to_excel(writer, sheet_name='EMG', header=['Time','EMG','env(EMG)','hilbert(EMG)'], index=False)
# end of file