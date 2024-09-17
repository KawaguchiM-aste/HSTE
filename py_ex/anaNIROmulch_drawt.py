# anaNIROmulch_drawt.py
# usage: python anaNIROmulch_drawt.py <ExcelFileName> <Mode>
# e.g. : python anaNIROmulch_drawt.py NIROnmSample_prepro 41
# <Mode>: [8] 8ch x2, [16] 16ch, [41] 4ch x2(Frontal), [42] 4ch x2(Temporal)
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
import anaNIRO2ch

pos8ch=np.array([[2,1,9,10],[4,3,11,12],[6,5,13,14],[8,7,15,16]])
pos16ch=np.array([[10,12,14,16],[9,11,13,15],[2,4,6,8],[1,3,5,7]])
pos4chF=np.array([[4,2,6,8],[3,1,5,7]])
pos4chT=np.array([[2,1,5,6],[4,3,7,8]])

def funcRMS(x):
    nd = len(x)
    RMS = 
    return RMS

if __name__=='__main__':
    args = sys.argv
    fname = args[1]
    mode = int(args[2])
    print('... Loading {}'.format(args[1]))
    datOHb = 
    datHHb = 
    datMask = 
    tEvent = 
    print('t_event[s]=')
    
    t = datOHb[0]
    dt = np.mean(np.diff(t))
    Fs = 1/dt
    Nch = datOHb.shape[1]-1
    tmpO = np.array(datOHb.loc[:,1:])
    tmpH = np.array(datHHb.loc[:,1:])
    
    resRMS = np.zeros((Nch,5))
    if mode==8:
        pos=pos8ch
    elif mode==16:
        pos=pos16ch
    elif mode==41:
        pos=pos4chF
    elif mode==42:
        pos=pos4chT
    
    for i in range(Nch):
        tmp = np.where(pos==i+1)
        
        
        
        
        
        ii=xx*plotCol + yy+1
        plt.subplot(plotRow,plotCol,ii)
        xO = tmpO[:,i]
        xH = tmpH[:,i]
        plt.plot(t,xO,'r')
        plt.plot(t,xH,'b')
        for tE in tEvent:
            plt.plot([tE, tE],yrange,'k--')
        plt.title('ch.{}'.format(i+1))
    plt.pause(5)
    t_start=input('t_start: ')
    t_start=float(t_start)
    it_start=
    plt.pause(2)
    t_end=input('t_end: ')
    t_end=float(t_end)
    it_end=int(Fs*t_end)
    for i in range(Nch):
        resRMS[i,3]=
        resRMS[i,4]=
        plt.subplot(plotRow,plotCol,i+1)
        plt.plot([t_start, t_start],yrange,'c--')
        plt.plot([t_end, t_end],yrange,'c--')
    plt.pause(2)
    plt.savefig('{}_time.png'.format(fname[:-7]))
    exfname='{}_RMS.xlsx'.format(fname[:-7])
    df=pd.DataFrame(resRMS)
    with pd.ExcelWriter(exfname, engine='openpyxl') as writer:
        
# end of file