# import pandas
#
#
# web_stats = {'Day':[1,2,3,4,5,6],
#              'Visitors':[43,34,65,56,29,76],
#              'Bounce Rate':[65,67,78,65,45,52]}
# print(web_stats)
#
# df = pandas.DataFrame(web_stats)
#
# print(df)
# for _func in [lambda :x*2 for x in range(2)]:
#     print(_func())

# import pandas as pd
# df1 = pd.DataFrame(
#     data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     index=[1, 2, 3],
#     columns=['a', 'b', 'c']
# )
# df2 = pd.DataFrame(
#     data=[[11, 22, 33], [44, 55, 66], [77, 88, 99]],
#     index=[4, 5, 6],
#     columns=['a', 'b', 'c']
# )
#
# df3 = df1.append(df2)
# columns = df3[['c']][(df3.c>= 9)]
# print(columns)

# import numpy as np
#
# a = np.linspace(1,40,30)
# print(a)


t = (2, 4, [6, 8])
t[-1].append(7)
print(t[-1])
t[-1] += [9]
print(t[-1])