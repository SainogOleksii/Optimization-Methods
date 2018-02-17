import numpy as np
import pandas as pd
import TargetFunction as Tf
import plotly
import plotly.graph_objs as go


def descent_method(conditions):
    h_fun, fun, f = conditions
    eps = 1e-6
    beta = 1
    alpha = 0.5
    x = np.zeros(3)
    tf = Tf.TargetFunction(fun, eps=0.1)

    dat = [[x, np.linalg.norm(tf.df_f(x)), tf.funсtion(x), 0, 0]]

    while True:
        h = h_fun(tf, x)
        alpha_k = f(tf, x, h, alpha=alpha, beta=beta)
        x_next = x + alpha_k * h
        dat.append([x_next,
                    np.linalg.norm(tf.df_f(x)),
                    tf.funсtion(x_next),
                    np.linalg.norm(x - x_next),
                    alpha_k])
        if (np.linalg.norm(x - x_next) < eps) & (np.linalg.norm(tf.df_f(x)) < eps):
            break
        x = x_next
    result = pd.DataFrame(data=np.array(dat), columns=['x', '|| F\'(x) ||', 'F(x)', 'Residual', 'alpha'])

    return result


def show_graphic(df, number):
    trace0 = go.Scatter(x=df.index, y=df['|| F\'(x) ||'], name='norma(F\'(x))')
    trace1 = go.Scatter(x=df.index, y=df['Residual'], name='delta(x_k)')
    trace2 = go.Scatter(x=df.index, y=df['F(x)'], name='F(x)')
    trace3 = go.Scatter(x=df.index, y=df['alpha'], name='a_k')
    layout = {'title': 'Residuals and function'}
    fig = go.Figure(data=[trace0, trace1, trace2, trace3], layout=layout)
    plotly.offline.plot(fig, filename='laba' + number + '.html', show_link=False)
