import time

start = time.time()
for i in range(6):
    time.sleep(1)
    print(i)
print(time.time() - start)

local_time = time.asctime(time.localtime(time.time()))
print(local_time)