import os
import time
import sys
reps = int(sys.argv[1])
n=15
k=6

for steep_checks in range(1, n+1):
    print("Number of genes being checked in steepLearn: {}".format(steep_checks))
    os.system('time python simulate.py '+str(k)+' '+str(reps)+' '+str(steep_checks)+' &')
    time.sleep(1)