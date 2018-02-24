from TargetFunction import df_tf


def h_gradient(tf, x):
    return - df_tf(tf, x)
