import os
import time
import sys
reps = int(sys.argv[1])
n=15
for k in range(n):
    print("K:",k)
    os.system('time python simulate.py '+str(k)+' '+str(reps)+' &')
    time.sleep(1)
