# def merge_sort(alist):
#     if len(alist) <=1 :
#         return alist
#     #二分分解
#     num = len(alist)//2
#
#     left = merge_sort(alist[:num])
#     right = merge_sort(alist[num:])
#
#     return merge(left,right)
#
# def merge(left,right):
#     l, r = 0,0
#     result = []
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result += left[l:]
#     result += right[r:]
#     return result
#
# alist = [20,42,5,11,45,23,12,76]
# sorted_alist = merge_sort(alist)
# print(sorted_alist)
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(set(a)))
print(list(dedupe(a)))