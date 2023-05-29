from abc import ABC, abstractclassmethod


# Abstract Class for Model a Basic Template for Implementation
class Model(ABC):
    def __init__(self, cues : list) -> None:
        super().__init__()
        self.cues = cues
        
    

    @abstractclassmethod
    def gradient_cue(self, cue):
        # Finite Difference Gradient
        pass

    