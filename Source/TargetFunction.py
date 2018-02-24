import numpy as np
eps = 1e-7


def df_tf(f, x):
    l = list()
    for i in np.eye(len(x)):
        l.append(df(f, x, i * eps, eps))
    return np.array(l)


def ddf_tf(f, x):
    size = len(x)
    mat = np.zeros((size, size))
    h = np.eye(len(x))
    h *= eps
    for i in range(size):
        for j in range(i + 1):
            if i == j:
                mat[i][j] = d2f_xx(f, x, h[i], eps)
            else:
                mat[i][j] = d2f_xy(f, x, [h[i], h[j]], eps)
    return mat


def function_a(a, fun=None, h=0, x=0):
    return fun(x + a * h)


def df(f, x, h, h1):
    return (f(x + h) - f(x - h)) / (2 * h1)


def d2f_xx(f, x, h, h1):
    return (f(x + h) + f(x - h) - 2 * f(x)) / h1 ** 2


def d2f_xy(f, x, h, h1):
    return (f(x + h[0] + h[1]) +
            f(x - h[0] - h[1]) -
            f(x - h[0] + h[1]) -
            f(x + h[0] - h[1])) / (4 * h1)
