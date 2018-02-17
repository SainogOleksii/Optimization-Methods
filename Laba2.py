import numpy as np


def alpha_search_lab2(tf, arg, h, alpha, beta):
    e = 1e-16
    eps = 1e-1
    i = beta
    while tf.funсtion(tf, arg + i * h) - \
            tf.funсtion(tf, arg) - \
            eps * i * np.dot(tf.df_f(tf, arg), h) > e:
        i *= alpha
    return i


def alpha_quick_lab2():
    pass


def h_2(tf, x):
    return - np.dot(np.linalg.inv(tf.ddf(tf, x)), tf.df_f(tf, x))
