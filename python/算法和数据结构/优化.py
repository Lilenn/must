# 优化三重循环

import time
start_time = time.time()
count = 0
for a in range(0,1001):
    for b in range(0,1001- a):
        c = 1000 - a - b
        count += 1
        if a**2 + b**2 == c**2 :
            print(a , b ,c )

end_time = time.time()
print(count)
print(end_time - start_time)
