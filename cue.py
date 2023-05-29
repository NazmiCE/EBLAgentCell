from abc import ABC, abstractclassmethod


class Cue(ABC):
    def __init__(self, type : str, grid) -> None:
        super().__init__()
        self.typeC = type
        self.grid = grid

    @abstractclassmethod
    def return_probability(self):
        # An interaction with environment should be implemented in the real class
        pass

    def __repr__(self) -> str:
        return self.typeC
    
    @ abstractclassmethod
    def return_gradient(self):
        pass