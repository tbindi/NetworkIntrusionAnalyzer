from numpy import exp, max, sum, array, mean, log


def sigmoid(i):
    return 1. / (1 + exp(-i))


# Made Static Functions
def softmax(i):
    sf = exp(i - max(i))
    if sf.ndim == 1:
        return sf / sum(sf, axis=0)
    else:
        return sf / array([sum(sf, axis=1)]).T


def entropy_mlr(y, sig):
    return -mean(sum(y * log(sig) + (1 - y) * log(1 - sig), axis=1))