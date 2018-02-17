import numpy as np
import TargetFunction as Tf


def fun(x):
    return 16 * x[0] ** 2 + 0.018 * x[0] * x[1] + 15 * x[1] ** 2 + 2 * x[2] ** 2 + x[0] - x[2]


tf = Tf.TargetFunction(fun)
print(
    tf.ddf(
        np.array([1, 1, 1])
    )
)
