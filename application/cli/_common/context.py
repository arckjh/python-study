from abc import *

class Context(metaclass=ABCMeta): 
    
    @abstractmethod
    def run(self, cmd=''):
        pass