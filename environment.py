from abc import ABC, abstractclassmethod
import numpy as np
from agent import Agent


# Discrete Environment
# Abstract Class for Environment a Basic Template for Implementation
# Will have cell locations in a grid no visual, visualization can be implemented in the main/or here with pygame, seaborn, matplotlib

class Environment(ABC):
    def __init__(self, agent_grid = None) -> None:
        super().__init__()
        self.agent_grid = agent_grid # Agents for kd tree search   
        self.agents = [] # All agents 
    
    def add_agent(self, list_agent: list):
        self.agents += list_agent
    
    def remove_agent(self, agent: Agent):
        pass

    @property
    def neigbouring_agents(self, agent):
        pass    
    
        

