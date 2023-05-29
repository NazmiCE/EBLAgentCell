from abc import ABC, abstractclassmethod
import itertools

# Abstract Class for Agent a Basic Template for Implementation
class Agent(ABC):
    iditer = itertools.count()
    def __init__(self) -> None:
        self.id = next(self.iditer) # Custom ID for every agents
        pass

    @abstractclassmethod
    def set_position(self, func):
        """
        func -> function
        This function takes a function as parameter (named as func), then the position of the agent is determined
        """
        pass

    @abstractclassmethod
    def make_decision(self, func):
        func()
        pass


    # When to print Cell Object for Debugging Purposes This Can be Utilized
    def __repr__(self) -> str:
        return "#" + str(self.id) + ": Cell"
    
    
