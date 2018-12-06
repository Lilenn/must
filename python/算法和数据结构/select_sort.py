def selection_sort(alist):
    '''选择排序'''
    n = len(alist)
    #需要进行n-1次选择操作
    for i in range(n-1):
        #记录最小元素的位置
        min_index = i
        #从i+1位置到末尾选择最小的数据
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j

        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]

alist = [12,56,34,10,90,44]
selection_sort(alist)
print(alist)