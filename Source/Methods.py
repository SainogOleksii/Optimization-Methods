from Laba1 import h_gradient
from Laba2 import h_newton
from Fibonacci import fibonacci, fibonacci_inverse
from functools import partial
from TargetFunction import df_tf, function_a
import numpy as np
import pandas as pd


def descent_method(tf, method='newton', coefficient='quick', start_point=None, with_start_point=False, n=1):
    if method == 'newton':
        h_fun = h_newton
    elif method == 'gradient':
        h_fun = h_gradient
    else:
        h_fun = None

    if coefficient == 'dividing':
        alpha = alpha_search_dividing
    elif coefficient == 'quick':
        alpha = alpha_search_quick
    else:
        alpha = None

    eps = 1e-7
    x = start_point if with_start_point else np.zeros(n)
    dat = list()
    while True:
        method = h_fun(tf, x)
        alpha_k = alpha(tf, x, method)
        x_next = x + alpha_k * method
        dat.append([x_next,
                    np.linalg.norm(df_tf(tf, x)),
                    tf(x_next),
                    np.linalg.norm(x - x_next),
                    alpha_k])
        if (np.linalg.norm(x - x_next) < eps) & (np.linalg.norm(df_tf(tf, x)) < eps):
            break
        x = x_next
    result = pd.DataFrame(
        data=np.array(dat),
        columns=['x', '|| F\'(x) ||', 'F(x)', 'Residual', 'alpha']
    )
    return result


def alpha_search_dividing(tf, arg, method):
    beta = 1
    alpha = 0.5
    e = 1e-32
    i = beta
    while tf(arg + i * method) - tf(arg) > e:
        i *= alpha
    return i


def alpha_search_quick(tf, arg, h):
    fun = partial(function_a, x=arg, h=h, fun=tf)
    return fibonacci_method(fun, 0, 1)


def fibonacci_method(tf, a, b, eps=1e-7):
    start_n = fibonacci_inverse((b - a) / eps) + 1
    if start_n > 90:
        return None
    lamb = a + (fibonacci(start_n - 2) / fibonacci(start_n)) * (b - a)
    meu = a + (fibonacci(start_n - 1) / fibonacci(start_n)) * (b - a)
    for i in range(start_n - 2):
        f_lamb = tf(lamb)
        f_meu = tf(meu)
        if f_lamb > f_meu:
            a = lamb
            lamb = meu
            meu = a + fibonacci(start_n - 2 - i) / fibonacci(start_n - 1 - i) * (b - a)
        else:
            b = meu
            meu = lamb
            lamb = a + fibonacci(start_n - 3 - i) / fibonacci(start_n - 1 - i) * (b - a)
    meu = lamb + eps ** 2
    f_lamb = tf(lamb)
    f_meu = tf(meu)
    if f_lamb > f_meu:
        a = lamb
    else:
        b = meu
    return (a + b) * 0.5
