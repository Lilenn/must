# def quict_sort(alist,start,end):
#     '''快速排序'''
#
#     #递归的退出条件
#     if start >= end:
#         return
#
#     #设定一个基准元素
#     mid = alist[start]
#
#     low = start
#     high = end
#
#     while low < high:
#         #如果low跟 high 没有重合，high指向的元素不比基准元素小，则high向左移动
#         while low < high and alist[high] >=mid:
#             high -= 1
#         #将high指向的元素放到low的位置上
#         alist[low] = alist[high]
#
#         while low < high and alist[low] < mid:
#             low += 1
#         alist[high] = alist[low]
#     alist[low] = mid
#     quict_sort(alist,start,low-1)
#     quict_sort(alist,low+1,end)
#
# alist = [23,13,45,23,65,25,67,2,46,3]
# quict_sort(alist,0,len(alist)-1)
# print(alist)

# def fibo(n):
#     if n<3:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# for i in range(10):
#     print(fibo(i))




