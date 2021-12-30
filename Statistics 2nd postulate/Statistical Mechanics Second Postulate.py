import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
class particles():
    objects=[]
    box=list(range(10))
    stat={}
    for b in box:
        stat[b]=0
    def __init__(self):
        self.box=1
        self.temp=1
        particles.objects.append(self)

    @classmethod
    def update(cls):
        for particle in cls.objects:
            randombit=np.random.binomial(1,0.2)
            if randombit==1:
                particle.box=random.choice([0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,7,7,7,8,8,8,9,9])
            
    @classmethod
    def stat1(cls):
        particles.clear()
        for particle in cls.objects:
            cls.stat[particle.box]+=1
    @classmethod
    def clear(cls):
        for keys in cls.stat.keys():
            cls.stat[keys]=0
N=int(input("enter N : "))
for i in range(N):
    particles()

def updatef(i,plotdata):
    particles.stat1()
    ax.clear()
    ax.set_xlim(-1,10)
    ax.set_ylim(0,N/2)
    plotdata[0]=plt.bar(particles.box,list(particles.stat.values()))
    particles.update()
    


figure=plt.figure()
ax=plt.axes()
ax.set_xlim(-1,10)
ax.set_ylim(0,N/3)
ax.set_title("Statistical Nature")
x=list(particles.stat.keys())
y=list(particles.stat.values())
plotdata=[plt.bar(x,y)]
import os
os.chdir('D:\Python code')

animat=animation.FuncAnimation(figure,updatef,200,fargs=(plotdata,),interval=10)
plt.show()            
            
        
        
    
