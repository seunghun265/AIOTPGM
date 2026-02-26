import numpy as np
import time

x=np.arange(1,10001)
y=np.arange(10001,20001)

start_time = time.time()
z=np.zeros_like(x)
for i in range(10000):
    z[i]=x[i]+y[i]

print(f"소요시간:{time.time()-start_time}초")

start_time = time.time()
z = x + y
print(f"소요시간:{time.time()-start_time}초")