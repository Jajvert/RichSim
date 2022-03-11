import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#ditto for hits from opticks
opticks_hits = open("build/Opticks_hits.txt","r")
hits = []
for line in opticks_hits:
    hits.append( [float(s) for s in line.strip().split()] )
    
hits = np.array(hits)

op_count = [0,0,0,0]
for r in hits:
    if(r[1]<650 and r[1]>100 and r[2]>2000 and r[2]<2300):
        op_count[0]+=1 #checks first mirror
    elif(r[1]<1100 and r[1]>650 and r[2]<1300 and r[2]>1000):
        op_count[1]+=1 #checks second mirror
    elif(r[1]<1300 and r[1]>1100 and r[2]>1200 and r[2]<1550):
        op_count[2]+=1 #checks that thing in front of detector
    elif(r[1]<1600 and r[1]>1350 and r[2]>1400 and r[2]<1700):
        op_count[3]+=1 #checks detector

fig = plt.figure()
    
ax = fig.add_subplot(111, projection='3d')
fig.set_size_inches(6, 6)

ax.scatter(hits[:,0],hits[:,1],hits[:,2],s=5,color='black',label='Detector Opticks: '+str(op_count[3])+' hits')
ax.legend(loc='best')


#ax.set_ylim3d(255, 275)
#ax.set_zlim3d(1310, 1330)
#ax.set_xlim3d(-100, 100)

plt.title("Hits collected by Opticks")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.savefig("plotHits.pdf")
plt.show()
    
