# anaECG.py
# usage: python anaECG.py <ExcelFileName>
# e.g. : python anaECG.py ECGsample
# required file: anaPSD.py

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sys
from biosppy.signals import ecg
import random
from scipy import interpolate
import anaPSD

def func_detect_R(x, t, sw=0, fname_export='resultRtimings'):
    t_win = 5
    dt = 
    Fs = 
    out = 
    y = 
    tR = 
    tshow=(np.max(t)-t_win)*random.random()
    itshow=[int(tshow*Fs),int((tshow+t_win)*Fs)]
    plt.figure(figsize=[8,5])
    plt.subplot(2,1,1)
    plt.plot(t,x,'k-',alpha=0.2)
    plt.plot(t,y,'b')
    plt.plot(t[itshow[0]:itshow[1]],y[itshow[0]:itshow[1]],'r')
    plt.ylabel('V_ECG')
    plt.xlim(np.min(t),np.max(t))
    plt.subplot(2,1,2)
    plt.plot(t,x,'k-',alpha=0.2)
    plt.plot(t,y,'r')
    plt.ylabel('V_ECG')
    for tt in tR:
        i = int(tt*Fs)
        if 
            plt.text(t[i],y[i],'R')
    plt.xlim(tshow, tshow+t_win)
    plt.xlabel('Time [s]')
    plt.pause(1)
    if sw==1:
        plt.savefig('{}_R.png'.format(fname_export)) 
    return tR

def func_draw_hist(x):
    bw = 
    bin = np.arange(np.min(x), np.max(x), bw)
    nbin = bin.shape[0]
    plt.

def func_RRI_stat(tR, sw=0, fname_export='resultRRI'):
    RRI = 
    tR = 
    mRRI = 
    SD_RRI = 
    s='RRI: Mean={:.3f}[s], SD={:.3f}[s]'.format(mRRI, SD_RRI)
    if sw==1:
        plt.figure(figsize=[8,2])
        plt.stem(tR, RRI)
        plt.xlabel('Time [s]')
        plt.ylabel('RRI[s]')
        plt.figure(figsize=[8,3])
        plt.subplot(1,2,1)
        plt.boxplot(RRI, labels=[' '], showmeans=True)
        #plt.scatter(np.ones(len(RRI)),RRI,c='blue',s=10,alpha=0.2)
        #plt.plot(tR, RRI)
        plt.ylabel('RRI[s]')
        #plt.xlabel('Time [s]')
        plt.subplot(1,2,2)
        func_draw_hist(RRI)
        plt.xlabel('# of RRI')
        plt.title(s)
        plt.pause(3)
        plt.savefig('{}_RRIstat.png'.format(fname_export))
    return mRRI, SD_RRI

def func_interp(tR, Fs=2.5, algo='linear', sw=0):
    # algo: 'linear', 'nearest', 'cubic', 'lagrange'
    RRI = np.diff(tR)
    dt = 1/Fs
    t = np.arange(tR[1], np.max(tR), dt)
    if algo=='lagrange':
        f = interpolate.lagrange(tR[1:], RRI)
    else:
        f = 
    RRIT = f(t)
    if sw==1:
        plt.figure(figsize=[8,2])
        plt.plot(tR[1:],RRI,'cs', alpha=0.6, label='RRI')
        plt.
        plt.xlabel('Time [s]')
        plt.ylabel('RRI [s]')
        plt.legend()
        plt.pause(1)
    return RRIT, t

def func_fft(x, t):
    dt = np.mean(np.diff(t))
    Fs = 1/dt
    n = len(x)
    n_half = int(n/2)
    fftx = np.fft.fft(x-np.mean(x))
    Y = (fftx*np.conj(fftx))/n_half
    Y = Y[0:n_half]
    f = np.linspace(0, Fs/2, n_half)
    plt.plot(f, np.real(Y))
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('PSD')
    plt.xscale('log')
    plt.xlim(0.01, 0.5) #追加
    plt.grid()
    plt.show()
    return Y, f

def funcPP(tR,sw=0,fname_export='resultPoincare'):
    RRI = 
    nRRI = 
    RRI1 = 
    RRI2 = 
    X1 =
    X2 =
    SD1 = 
    SD2 = 
    s = 'SD1={:.4f}, SD2={:.4f}'.format(SD1,SD2)
    cx = np.mean(RRI1)
    cy = np.mean(RRI2)
    if sw==1:
        sq2=np.sqrt(2)
        plt.figure()
        plt.plot(RRI1, RRI2, 'bo', alpha=0.2)
        plt.xlabel('RRI(k)')
        plt.ylabel('RRI(k+1)')
        plt.title(s)
        plt.plot([cx,cx+SD2/sq2], [cy,cy+SD2/sq2],'--')
        plt.plot([cx-SD1/sq2,cx],[cy+SD1/sq2,cy],'--')
        plt.axis('equal')
        plt.pause(1)
        plt.savefig('{}_Poincare.png'.format(fname_export))
    return SD1,SD2

def funcRRIT(t,x,Fs_new,sw=0,fname_export='RRIT'):
    Fs = 
    out = 
    tR = out[2]*(1/Fs)
    RRI = 
    tR = tR[1:]
    dt = 1/Fs_new
    tnew = 
    RRIT = 
    n = len(tnew)
    if sw==1:
        X = np.concatenate([tnew.reshape(n,1), RRIT.reshape(n,1)],1)
        df = pd.DataFrame(X)
        df.to_csv('{}_RRIT.csv'.format(fname_export), index=False, header=False)
    return tnew, RRIT

def funcLFHF(t,x,index=0,fname_ex='ECG_LFHF'):
    PSD = 
    LFHF = 
    Pabs,Prel = 
    s = 
    print(s)
    plt.subplot(2,1,1)
    plt.ylabel('RRI Trend[s]')
    plt.title(s)
    plt.savefig('{}_PSD.png'.format(fname_ex))
    return Pabs[0],Pabs[1],Prel[0],Prel[1]

if __name__=='__main__':
    args = sys.argv
    fname=args[1]
    print('... Loading {}'.format(args[1]))
    dat = pd.read_excel('{}.xlsx'.format(fname), sheet_name='raw')
    n = dat.shape[0]
    Nch = dat.shape[1]
    x = dat.values.reshape(n,Nch)
    t = x[:,0]
    Fs = 1/np.mean(np.diff(t))
    tR = 
    print('Fs={:.3f} Hz'.format(Fs))
    mRRI, sRRI = 
    SD1,SD2 = 
    tref,RRIT = 
    LF,HF,nLF,nHF = 
# end of file 
