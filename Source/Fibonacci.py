import numpy as np
from math import floor, log


def fibonacci(n):
    mat = np.array([[1, 1], [1, 0]])
    return matrix_pow(mat, n)[0][1]


def fibonacci_inverse(x):
    phi = (1 + 5 ** 0.5) / 2
    x = floor(x)
    arg = x * 5 ** 0.5 + (5 * x ** 2 + 4) ** 0.5
    return floor(log(arg) / log(phi)) - 1


def matrix_pow(matrix, n):
    if n == 0:
        n, m = matrix.shape
        return np.eye(n, m)
    elif n == 1:
        return matrix
    else:
        y = matrix_pow(matrix, n // 2)
        y = np.dot(y, y)
        if n % 2:
            y = np.dot(matrix, y)
        return y
