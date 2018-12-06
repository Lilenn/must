def bubble_sort(alist):
    for i in range(len(alist)-1,0,-1):
        #i 是表示每次遍历需要的次数，是逐渐减小的
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]

li = [32.12,45,56,33,70,23,90,45]
bubble_sort(li)
print(li)