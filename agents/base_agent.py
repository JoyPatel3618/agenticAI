from abc import ABC, abstractclassmethod
from core.logger import get_logger

class BaseAgent(ABC):
    def __init__(self,name):
        self.name = name
        self.logger = get_logger(name) 
    
    @abstractclassmethod
    def run(self,task):
        pass
