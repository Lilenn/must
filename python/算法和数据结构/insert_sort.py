def insert_sort(alist):
    #从第二个位置排序
    for i in range(1,len(alist)):
        #从第i个元素开始向前比较，如果小于前一个元素，那就交换位置
        for j in range(i,0 ,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]


alist = [45,32,16,67,78,34,10]
insert_sort(alist)
print(alist)

