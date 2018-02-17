from Methods import *


def alpha_search_lab1(tf, arg, h, alpha, beta):
    eps = 1e-16
    i = beta
    while tf.funсtion(arg + i * h) - tf.funсtion(arg) >= eps:
        i *= alpha
    return i


def alpha_quick_lab1(tf, arg, h):
    fun = Tf.TargetFunction(tf.f_alpha_k(x=arg, h=h))
    return descent_method((h_1, fun, alpha_search_lab1))


def h_1(tf, x):
    return - tf.df_f(x)
