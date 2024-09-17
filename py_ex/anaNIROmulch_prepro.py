# anaNIROmulch_prepro.py
# usage: python anaNIROmulch_prepro.py <.nm FileName> <# Channels>
# e.g. : python anaNIROmulch_prepro.py NIROnmSample 8
# Required files: funcFilter, anaNIRO2ch
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
import re
import random
import funcFilter
import anaNIRO2ch

twin = 10.0
FcL = 
FcH = 
Order = 4

if __name__=='__main__':
    args = sys.argv
    fname = args[1]
    Nch = int(args[2])
    print('... Loading {}'.format(args[1]))
    dat = pd.read_csv('{}.nm'.format(fname), header=1)
    t=dat['elpsec']
    nd=len(t)
    dt=np.mean(np.diff(t))
    Fs=1/dt
    Fnq=Fs/2
    OHb = np.empty((nd,Nch))
    HHb = np.empty((nd,Nch))
    MaskERR = np.ones((nd,Nch))
    TypeERR = np.zeros((nd,Nch))
    F = funcFilter.bwfilter()
    OHbrev = np.empty((nd,Nch))
    HHbrev = np.empty((nd,Nch))
    for i in range(Nch):
        OHb[:,i]=eval('dat[\'O2Hb_{}\']'.format(i+1))
        HHb[:,i]=eval('dat[\'HHb_{}\']'.format(i+1))
        OHbrev[:,i]=F.funcBPF(OHb[:,i], FcL, FcH, Fs, Order)
        HHbrev[:,i]=F.funcBPF(HHb[:,i], FcL, FcH, Fs, Order)
    ERR=dat['Comment']
    tEvent = anaNIRO2ch.funcdetectEvent(t,ERR)
    print(tEvent)
    
    # Error detection
    for it in range(nd):
        s=re.findall(r'P\d+_E\d',ERR[it])
        if len(s)>0:
            for i in range(len(s)):
                val=re.findall(r'\d+',s[i])
                ch = int(val[0])
                errtype = int(val[1])
                MaskERR[it,ch-1]=nan
                TypeERR[it,ch-1]=errtype
    
    # Export Sample Fig.
    chshow = random.randint(0, Nch-1)
    tshow = (np.max(t)-twin)*random.random()
    itshow = int(tshow*Fs)
    itwin = int(twin*Fs)
    plt.subplot(2,2,1)
    plt.plot(t, OHb[:,chshow],'r',alpha=0.3)
    plt.plot(t[itshow:itshow+itwin], OHb[itshow:itshow+itwin,chshow],'r')
    plt.title('Raw OHb@ch.{}'.format(chshow+1))
    plt.subplot(2,2,3)
    plt.plot(t[itshow:itshow+itwin], OHb[itshow:itshow+itwin,chshow],'r')
    plt.xlim(tshow, tshow+twin)
    plt.xlabel('Time [s]')
    plt.subplot(2,2,2)
    plt.plot(t, OHbrev[:,chshow],'r',alpha=0.3)
    plt.plot(t[itshow:itshow+itwin], OHbrev[itshow:itshow+itwin,chshow],'r')
    plt.title('Filtered (Fc=[{}, {}]Hz,order={})'.format(FcL,FcH,Order))
    plt.subplot(2,2,4)
    plt.plot(t[itshow:itshow+itwin], OHbrev[itshow:itshow+itwin,chshow],'r')
    plt.xlim(tshow, tshow+twin)
    plt.xlabel('Time [s]')
    plt.pause(5)

    # Export data
    exfname='{}_prepro.xlsx'.format(fname)
    t=np.array(t)
    t=t.reshape((nd,1))
    tEvent=tEvent.reshape((len(tEvent),1))
    dfOHb=pd.DataFrame(np.concatenate([t, OHbrev], 1))
    dfHHb=pd.DataFrame(np.concatenate([t, HHbrev], 1))
    dfMask=pd.DataFrame(np.concatenate([t, MaskERR], 1))
    dfType=pd.DataFrame(np.concatenate([t, TypeERR], 1))
    dfEvent=pd.DataFrame(tEvent)
    with pd.ExcelWriter(exfname, engine='openpyxl') as writer:
        dfOHb.to_excel(writer, sheet_name='OHb', index=False, header=False)
        dfHHb.to_excel(writer, sheet_name='HHb', index=False, header=False)
        dfMask.to_excel(writer, sheet_name='ErrorMask', index=False, header=False)
        dfType.to_excel(writer, sheet_name='ErrorType', index=False, header=False)
        dfEvent.to_excel(writer, sheet_name='tEvent', index=False, header=False)
# end of file