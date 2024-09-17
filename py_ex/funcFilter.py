import numpy as np
from scipy.signal import butter, lfilter

class bwfilter:
    def funcLPF(self, x, Fc, Fs, order=4):
        Fnq = Fs/2
        nFc = Fc/Fnq
        b,a = butter(order, nFc, btype='low', analog=False)
        y = lfilter(b,a,x)
        return y
    
    def funcHPF(self, x, Fc, Fs, order=4):
        Fnq = Fs/2
        nFc = Fc/Fnq
        b,a = butter(order, nFc, btype='high', analog=False)
        y = lfilter(b,a,x)
        return y
		
    def funcBPF(self, x, Fc1, Fc2, Fs, order=4):
        Fnq = Fs/2
        nFc1 = Fc1/Fnq
        nFc2 = Fc2/Fnq
        b,a = butter(order, [nFc1, nFc2], btype='bandpass', analog=False)
        y = lfilter(b,a,x)
        return y
	
    def funcBEF(self, x, Fc1, Fc2, Fs, order=5):
        Fnq = Fs/2
        nFc1 = Fc1/Fnq
        nFc2 = Fc2/Fnq
        b,a = butter(order, [nFc1, nFc2], btype='bandstop', analog=False)
        y = lfilter(b,a,x)
        return y
		
if __name__=='__main__':
    print('This is a module file')