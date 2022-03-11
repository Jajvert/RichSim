import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


g4_file = open("build/Geant4_hits.txt","r") #opens G4 file
g4_result = []
for line in g4_file: #iterates over lines in G4 file

    temp = [float(s) for s in line.strip().split()] #divides lines by commas
            
    g4_result.append(temp) #adds contents of line to g4_result

g4_result = np.array(g4_result) #converts array to numpy

g4_count = [0,0,0,0]

for r in g4_result:
    if(r[1]<650 and r[1]>100 and r[2]>2000 and r[2]<2300):
        g4_count[0]+=1 #checks first mirror
    elif(r[1]<1100 and r[1]>650 and r[2]<1300 and r[2]>1000):
        g4_count[1]+=1 #checks second mirror
    elif(r[1]<1300 and r[1]>1100 and r[2]>1200 and r[2]<1550):
        g4_count[2]+=1 #checks that thing in front of detector
    elif(r[1]<1600 and r[1]>1350 and r[2]>1400 and r[2]<1700):
        g4_count[3]+=1 #checks detector


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
fig.set_size_inches(5, 5)

ax.scatter(g4_result[:,0],g4_result[:,1],g4_result[:,2],s=5,color='blue',label='Detector Geant4: '+str(g4_count[3])+' hits')
ax.scatter(hits[:,0],hits[:,1],hits[:,2],s=5,color='black',label='Detector Opticks: '+str(op_count[3])+' hits')
ax.legend(loc='best')


ax.set_ylim3d(1350, 1600)
ax.set_zlim3d(1450, 1700)
ax.set_xlim3d(-125, 125)

ax.invert_xaxis()

plt.title("Hits collected by Opticks and Geant4")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.savefig("plotHits.pdf")
plt.show()
    
