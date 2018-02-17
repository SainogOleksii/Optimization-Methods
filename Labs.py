from Laba1 import *
from Laba2 import *
from Methods import *


def target_function(x):
    return 16 * x[0] ** 2 + 0.018 * x[0] * x[1] + 15 * x[1] ** 2 + 2 * x[2] ** 2 + x[0] - x[2]

# Writer to Excel format
writer = pd.ExcelWriter('MethOpt.xlsx', engine='xlsxwriter')

# List of labs
laba1 = (h_1, target_function, alpha_quick_lab1)
laba2 = (h_2, target_function, alpha_search_lab2)

# Launch
labs = [descent_method(laba1),
        descent_method(laba2)]
for i, j in enumerate(labs):
    j.to_excel(writer, 'Laba' + str(i + 1))
    show_graphic(j, str(i + 1))
writer.save()
writer.close()
