import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class LifeGame():
    def __init__(self,N):
        self.L = N
        self.field = np.zeros([self.L,self.L], dtype=int)
        self.next_field = np.zeros([self.L,self.L], dtype=int)
        
    def init(self,p):
        self.field = np.random.choice([0,1],
                    [self.L,self.L],p=[1-p,p])


    def environment(self,i,j):
        return [ [(i-1 + self.L)%self.L, (j-1 + self.L)%self.L],
                 [(i-1 + self.L)%self.L, (  j + self.L)%self.L],
                 [(i-1 + self.L)%self.L, (j+1 + self.L)%self.L],
                 [(  i + self.L)%self.L, (j-1 + self.L)%self.L],
                 [(  i + self.L)%self.L, (j+1 + self.L)%self.L],
                 [(i+1 + self.L)%self.L, (j-1 + self.L)%self.L],
                 [(i+1 + self.L)%self.L, (  j + self.L)%self.L],
                 [(i+1 + self.L)%self.L, (j+1 + self.L)%self.L]]


    def evolution(self):
        for i in range(self.L):
            for j in range(self.L):
                evlist = self.environment(i,j)
                evnum = sum([self.field[i[0],i[1]] for i in evlist])
                
                if self.field[i,j] == 0:
                    if evnum == 3:
                        self.next_field[i,j] = 1
                    else:
                        self.next_field[i,j] = 0
                elif self.field[i,j] == 1:
                    if evnum == 2 or evnum == 3:
                        self.next_field[i,j] = 1
                    elif evnum <= 1:
                        self.next_field[i,j] = 0
                    elif evnum >= 4:
                        self.next_field[i,j] = 0
                        
        self.field = self.next_field
        self.next_field = np.zeros([self.L,self.L], dtype=int)
        return self.field
    
def main():
    L = LifeGame(100)
    L.init(0.3)
    
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.set_ylim(0,100)
    ax.set_xlim(0,100)
    n = 100
    
    ims = []
    
    for i in range(n):
        ev_arr = L.evolution()
        pl_arr = np.array(np.where(ev_arr == 1))
        im=plt.plot(*pl_arr,"s",ms=2,c="r")
        ims.append(im)
     
    ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=1000)
    ani.save("LifeGame.gif",writer="imagemagick")