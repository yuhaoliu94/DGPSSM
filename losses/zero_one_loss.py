import numpy as np
from . import loss

class ZeroOneLoss(loss.Loss):
    def __init__(self, dout):
        loss.Loss.__init__(self,dout)

    def eval(self, ytrue, ypred):
        error_rate = np.mean(np.argmax(ypred, 1) != np.argmax(ytrue, 1))
        return error_rate

    def get_name(self):
        return "Error Rate"
