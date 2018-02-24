import numpy as np
from TargetFunction import df_tf, ddf_tf


def h_newton(tf, x):
    return - np.dot(np.linalg.inv(ddf_tf(tf, x)), df_tf(tf, x))
