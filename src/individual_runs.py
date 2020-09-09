import numpy as np
import matplotlib.pyplot as plt


new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']

reps = 5000
condNum = 7

bh = np.zeros((reps,condNum,100))
ah = np.zeros((reps,condNum,100))

bh = np.load("5000/steepest/nonlamarckian/bh_6.npy")
ah = np.load("5000/steepest/nonlamarckian/ah_6.npy")

c=0
b = bh[1,c,:].T
a = ah[1,c,:].T
plt.plot(b,'k',alpha=0.25)
np.savetxt("Figures/c0_b_i.dat",b,delimiter=',')
np.savetxt("Figures/c0_a_i.dat",a,delimiter=',')
plt.plot(a,'y',alpha=0.25)
b = np.mean(bh[:,c,:],axis=0).T
a = np.mean(ah[:,c,:],axis=0).T
np.savetxt("Figures/c0_b_m.dat",b,delimiter=',')
np.savetxt("Figures/c0_a_m.dat",a,delimiter=',')
plt.plot(b,'k')
plt.plot(a,'y')
plt.xlabel("Learning events")
plt.ylabel("Fitness")
plt.show()

c=6
b = bh[0,c,:].T
a = ah[0,c,:].T
plt.plot(b,'k',alpha=0.25)
plt.plot(a,'y',alpha=0.25)
np.savetxt("Figures/c6_b_i.dat",b,delimiter=',')
np.savetxt("Figures/c6_a_i.dat",a,delimiter=',')
b = np.mean(bh[:,c,:],axis=0).T
a = np.mean(ah[:,c,:],axis=0).T
plt.plot(b,'k')
plt.plot(a,'y')
np.savetxt("Figures/c6_b_m.dat",b,delimiter=',')
np.savetxt("Figures/c6_a_m.dat",a,delimiter=',')
plt.xlabel("Learning events")
plt.ylabel("Fitness")
plt.show()

c=3
b = bh[0,c,:].T
a = ah[0,c,:].T
plt.plot(b,'k',alpha=0.25)
plt.plot(a,'y',alpha=0.25)
np.savetxt("Figures/c3_b_i.dat",b,delimiter=',')
np.savetxt("Figures/c3_a_i.dat",a,delimiter=',')
b = np.mean(bh[:,c,:],axis=0).T
a = np.mean(ah[:,c,:],axis=0).T
plt.plot(b,'k')
plt.plot(a,'y')
np.savetxt("Figures/c3_b_m.dat",b,delimiter=',')
np.savetxt("Figures/c3_a_m.dat",a,delimiter=',')
plt.xlabel("Learning events")
plt.ylabel("Fitness")
plt.show()
