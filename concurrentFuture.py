import time
import concurrent.futures

def sum(a,b):
    total=0
    for i in range(a,b):
        total+=i
    return total
 
time1=time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=i) as executor:
    future = executor.submit(sum, 1, 10000000)
    print(time.time()-time1) //0.006593227386474609
