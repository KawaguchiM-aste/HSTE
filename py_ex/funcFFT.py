import numpy as np

class funcFFT:
  def ampSpect(self, x, Fs):
    dt = 1/Fs
    N = len(x)
    Nhalf = int(N/2)
    X = 
    Y = 
    f = np.linspace(0, Fs/2, Nhalf)
    return Y[0:Nhalf], f

if __name__=='__main__':
  print('This is a module file')
# end of file