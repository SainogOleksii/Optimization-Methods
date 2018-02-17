import numpy as np


class TargetFunction:
    def __init__(self, f, eps=1e-5):
        self.f = f
        self.eps = eps

    def funсtion(self, h):
        return self.f(h)

    def df_f(self, x):
        l = list()
        for i in np.eye(len(x)):
            l.append(df(self.f, x, i * self.eps, self.eps))
        return np.array(l)

    def ddf(self, x):
        size = len(x)
        mat = np.zeros((size, size))
        h = np.eye(len(x))
        h *= self.eps
        for i in range(size):
            for j in range(i + 1):
                if i == j:
                    mat[i][j] = d2f_xx(self.f, x, h[i], self.eps)
                else:
                    mat[i][j] = d2f_xy(self.f, x, [h[i], h[j]], self.eps)
        return mat

    def f_alpha_k(self, a, h=0, x=0):
        return self.funсtion(x + a * h)


def df(f, x, h, h1):
    return (f(x + h) - f(x - h)) / (2 * h1)


def d2f_xx(f, x, h, h1):
    return (f(x + h) + f(x - h) - 2 * f(x)) / h1 ** 2


def d2f_xy(f, x, h, h1):
    return (f(x + h[0] + h[1]) +
            f(x - h[0] - h[1]) -
            f(x - h[0] + h[1]) -
            f(x + h[0] - h[1])) / (4 * h1)
