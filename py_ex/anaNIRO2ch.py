# anaNIRO2ch.py
# usage: python anaNIRO2ch.py <.nx2 FileName>
# e.g. : python anaNIRO2ch.py NIRO2chSample

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sys
import re

def funcdetectEvent(t,dat):
    xEvent = 0
    nd = len(dat)
    

def funcMinMax(*dat):
    tmpMin = 0
    tmpMax = 0
    for v in dat:
        min = np.min(v)
        max = np.max(v)
        

def funcSavefig(t, OHb, HHb, TOI, tEvent, chNo, fname='resNIRS'):
    valMinMax = funcMinMax(OHb,HHb)
    dHb = OHb - HHb
    plt.figure(chNo)
    plt.subplot(3,1,1)
    plt.plot(t,OHb,color='r',label='OHb')
    plt.plot(t,HHb,color='b',label='HHb')
    plt.title('ch.{}'.format(chNo))
    plt.legend() 
    plt.ylabel('Hb [umol/L]')
    plt.subplot(3,1,2)
    plt.plot(t,dHb,color='orange')
    plt.ylabel('OHb-HHb [umol/L]')
    plt.subplot(3,1,3)
    plt.plot(t,TOI)
    plt.ylabel('TOI [%]')
    for i in range(3):
        plt.subplot(3,1,1+i)
        plt.grid()
        for timing in tEvent:
            if i<2:
                plt.plot([timing,timing],valMinMax,'k--')
            else:
                plt.plot([timing,timing],[60,100],'k--')
    plt.xlabel('Time [s]')  
    plt.pause(5)
    plt.savefig('{}_results_ch{}.png'.format(fname,chNo))

if __name__=='__main__':
    args = sys.argv
    fname=args[1]
    print('... Loading {}'.format(args[1]))
    