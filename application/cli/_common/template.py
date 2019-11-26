from abc import *

class Template(metaclass=ABCMeta): 
    
    @abstractmethod
    def input_data(self, **kwargs):
        pass
    
    @abstractmethod
    def input_error(self, **kwargs):
        pass
    
    @abstractmethod
    def output(self, **kwargs):
        pass