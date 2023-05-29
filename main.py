import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from agent import Agent
from model import Model
from environment import Environment
from cue import Cue


# WILL BE UPDATED LATER
# MESH GRID ORGANIZE LATER
xx = np.arange(0, 1000, 1)
yy = np.arange(0, 1000, 1)
xv, yv = np.meshgrid(xx,yy)

# A 2D region 
zz = np.stack((xv,yv,xv), axis = 2)


# CUES
class ChemicalCue(Cue):
    def __init__(self, grid, typeC = "Chemical"):
        super().__init__(typeC, grid)
        

    def return_probability(self):
        pass

    def return_gradient(self):
        return np.gradient(self.grid)
    
    def return_tendency(self, cell):
        gradient_y, gradient_x = self.return_gradient()
        return 0.13 * gradient_x[int(cell.y), int(cell.x)], 0.13 * gradient_y[int(cell.x), int(cell.y)]

"""class MechanicalCue(Cue):
    def __init__(self, typeC = "Mechanical") -> None:
        super().__init__(typeC)

    def return_probability(self):
        pass

    
    def return_gradient(self):
        pass
"""

# Agent
class Cell(Agent):
    def __init__(self, x, y, kind = "Normal"):
        super().__init__()
        self.x = x # Initialization of x position
        self.y = y # Initialization of y position 
        self.cycle = 0
        self.kind = kind

    ### set_position and make_decision will worked together

    # This method will be used constantly with different 
    # rules
    def set_position(self, func):
        
        # This function will evaluate the position displacement at the given time frame and environment conditions
        # A func() as parameter is needed and this is suitable for any appropriate form of functions
        xdisp, ydisp = func()  
        self.x += xdisp
        self.y += ydisp
        
    # This method will take rules as function and other
    # possible parameters such as neighboring cells
    # stiffness gradient etc as parameters 

    def make_decision(self, tendency : tuple):
        
        # I may need to couple Environment Model and given Agent together
        xtend, ytend = tendency
        xdisp = random.gauss(xtend, xtend/10 + 0.005) # xtend is averaged vector, xtend/10 stands for std a probabilistic approach but the parameter
                                              # is not taken from literature  
        ydisp = random.gauss(ytend, ytend/10 + 0.005) # Also maybe these parameters could be agent, and/or cue spesific for example
                                              # some type of cue induce more precise vector if this is the case tot_tendency_x and y should be changed also
                                              # the best practice would be to write more rules in model

        return (xdisp, ydisp)

    def mitosis(self, environment : Environment): # NOT FINISHED NOT NECESSARY UNTIL MULTI AGENT SYSTEMS
        pass 
    
    def adoptosis(self, environment : Environment): # NOT FINISHED NOT NECESSARY UNTIL MULTI AGENT SYSTEMS
        pass

# Model
class IntModel(Model):
    def __init__(self, cues):
        super().__init__(cues)

    def gradient_cue(self, cue : str):
        if cue in self.cues:
            return cue.return_gradient()
        
        else: 
            raise ValueError(f"Unknown Cue :{cue}. Try one of these {self.cues}")

# Environment
class System(Environment):
    def __init__(self, agent_grid=None) -> None:
        super().__init__(agent_grid)

# Stagnant Cells
stgCells = []
for i in range(3):
    for j in range(3):
        newCell = Cell(530 + i*10, 530 + j*10)
        stgCells.append(newCell)

# AGENT / CELL
cell1 = Cell(500,300) # Middle of the System

# System
syss = System()
syss.add_agent([cell1])



all_cells = syss.agents + stgCells

# MODEL

# Initializing a sample chemical gradient
# With the size of system afterwards those values can be stored as constants
chemical_gradient = np.zeros((1000,1000))



for i in range(0,1000):
    chemical_gradient[i,:] = i*10
    

chemicalCue = ChemicalCue(chemical_gradient)
intmodel = IntModel([chemicalCue])

fig, ax = plt.subplots()

scat = ax.scatter([cell.x for cell in all_cells],[cell.y for cell in all_cells], c = "black")
plt.imshow(chemical_gradient)
plt.colorbar()
        


# Simulation run
def main(frame):
        for i in syss.agents:
            #plt.scatter(i.x, i.y, color = "black")
            #plt.show()
            tot_tendency_x, tot_tendency_y = 0, 0
            for cue in intmodel.cues:
                tend_x, tend_y = cue.return_tendency(i)
                tot_tendency_x += tend_x
                tot_tendency_y += tend_y
            
            xdisp, ydisp = i.make_decision((tot_tendency_x,tot_tendency_y))
            i.x += xdisp
            i.y += ydisp
            print(i.x, i.y)
        print("***")
        scat.set_offsets([(cell.x, cell.y) for cell in all_cells])

if __name__ == "__main__":
    ani = FuncAnimation(fig, func=main, frames=500, interval=0.000000000000001)

    ani.save("ABM2.gif")

        
        
