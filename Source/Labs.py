from Methods import descent_method
import pandas as pd
import numpy as np
from math import floor
import plotly
import plotly.graph_objs as go


def show_graphic(df, number):
    trace0 = go.Scatter(x=df.index, y=df['|| F\'(x) ||'], name='norma(F\'(x))')
    trace1 = go.Scatter(x=df.index, y=df['Residual'], name='delta(x_k)')
    trace2 = go.Scatter(x=df.index, y=df['F(x)'], name='F(x)')
    trace3 = go.Scatter(x=df.index, y=df['alpha'], name='a_k')
    layout = {'title': 'Residuals and function'}
    fig = go.Figure(data=[trace0, trace1, trace2, trace3], layout=layout)
    plotly.offline.plot(fig, filename='../Result/Lab' + number + '.html', show_link=False)


def target_function(x):
    return 16 * x[0] ** 2 + 0.018 * x[0] * x[1] + 15 * x[1] ** 2 + 2 * x[2] ** 2 + x[0] - x[2]
rank = 3
point = np.zeros(rank)  # function description


# Writer to Excel format

writer = pd.ExcelWriter('../Result/MethOpt.xlsx', engine='xlsxwriter')


# List of labs
labs = list()
labs.append(descent_method(target_function, method='gradient', coefficient='dividing', n=rank))
labs.append(descent_method(target_function, method='gradient', n=rank, with_start_point=True, start_point=point))
labs.append(descent_method(target_function, coefficient='dividing', n=rank, with_start_point=True, start_point=point))
labs.append(descent_method(target_function, n=rank))


# Launch
for i, j in enumerate(labs):
    string = str(floor((i + 2) / 2)) + "_" + str(i % 2 + 1)
    j.to_excel(writer, 'Lab' + string)
    show_graphic(j, string)
writer.save()
writer.close()
