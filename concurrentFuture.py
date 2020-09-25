import time
import concurrent.futures

def sum(a,b):
    total=1
    for i in range(a,b):
        total = total + i
    print(time.time()-time1)
    return total

print("직렬 처리 시간:")

time1=time.time()

sum(1,10000000)
sum(1,10000000)
 
print("병렬 처리 시간:")

time1=time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=i) as executor:
    future = executor.submit(sum, 1, 10000000)
    future = executor.submit(sum, 1, 10000000)
