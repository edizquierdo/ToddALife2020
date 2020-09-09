import numpy as np

n=15
reps = 5000
condNum = 7

bh = np.zeros((n,reps,condNum,100))

for sc in range(1,n+1):
    bh[sc-1] = np.load("DiffStep_5000/lamarckian/bh_6_{}.npy".format(sc))

bh=np.mean(bh,axis=1)

np.savetxt("Figures/5000_diffsteep_lamarck.dat",np.max(bh,axis=2),delimiter=',')
