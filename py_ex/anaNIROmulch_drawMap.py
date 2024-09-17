# anaNIROmulch_drawMap.py
# usage: python anaNIROmulch_drawMap.py <ExcelFileName>
# e.g. : python anaNIROmulch_drawMap.py NIROnmSample_RMS
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
from scipy.interpolate import griddata

Nreso = 
Creso = 
method = 'cubic' # nearest, linear, cubic
levelO = 
levelH = 

if __name__=='__main__':
    args = sys.argv
    fname = args[1]
    print('... Loading {}'.format(args[1]))
    dat = pd.read_excel('{}.xlsx'.format(fname), sheet_name='RMS', header=None)
    chNo = dat[0]
    Nch = len(chNo)
    x = dat[1]
    y = dat[2]
    xy = dat.loc[:,1:2]
    OHb = 
    HHb = 
    xnew = 
    ynew = 
    xx,yy = np.meshgrid(xnew,ynew)
    zO = 
    zH = 
    plt.figure(1)
    plt.contourf
    plt.title('RMS(OHb)')
    plt.figure(2)
    plt.contourf
    plt.title('RMS(HHb)')
    for i in range(2):
        plt.figure(i+1)
        plt.colorbar()
        plt.
        for j in range(Nch):
            plt.
        plt.pause(2)
    plt.figure(1)
    
    plt.figure(2)
    
# end of file