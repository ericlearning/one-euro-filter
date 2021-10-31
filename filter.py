import numpy as np

def alpha(rate, cutoff):
    tau = 1 / (2 * 3.141592 * cutoff)
    te = 1 / rate
    return 1 / (1 + tau / te)

class LowPassFilter:
    def __init__(self):
        self.first_time = True
    
    def filter(self, x, alpha):
        if self.first_time:
            self.first_time = False
            self.hatxprev = x
        
        hatx = alpha * x + (1 - alpha) * self.hatxprev
        self.hatxprev = hatx
        return hatx

class OneEuro:
    def __init__(self, mincutoff, beta, dcutoff):
        self.first_time = True
        self.mincutoff = mincutoff
        self.beta = beta
        self.dcutoff = dcutoff
        self.dxfilt = LowPassFilter()
        self.xfilt = LowPassFilter()
        self.t = None
    
    def filter(self, x, t):
        if self.first_time:
            self.first_time = False
            dx = 0
            rate = 1 / 1e-7
        else:
            rate = 1 / (t - self.t)
            dx = (x - self.xfilt.hatxprev) * rate
        
        edx = self.dxfilt.filter(dx, alpha(rate, self.dcutoff))
        cutoff = self.mincutoff + self.beta * np.abs(edx)
        self.t = t
        return self.xfilt.filter(x, alpha(rate, cutoff))