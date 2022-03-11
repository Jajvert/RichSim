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


plt.scatter(g4_result[:,1],g4_result[:,2],s=5,color='blue',label='Geant4: '+str(g4_result.shape[0])+' hits')
plt.legend(loc='best')

#how many hit the first mirror:
plt.text(600,1900,"Geant4: "+str(g4_count[0]))

#second mirror
plt.text(1100,1000,"Geant4: "+str(g4_count[1]))

#thing in front of detector
plt.text(1100,1300,"Geant4: "+str(g4_count[2]))

#detector
plt.text(1600,1700,"Geant4: "+str(g4_count[3]))

plt.axis([0,1600,900,2300]) #plots axes

#plt.xticks(np.arange(0, 1600, 100))
#plt.yticks(np.arange(900, 2300, 100))

ax = plt.gca()

ax.invert_xaxis()

plt.title("Hits collected by Opticks and Geant4")
plt.xlabel("y")
plt.ylabel("z")

plt.savefig("plotHits.pdf")
plt.show()
    
