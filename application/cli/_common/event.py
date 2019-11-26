from abc import *

class Event(metaclass=ABCMeta):
    
    @abstractmethod
    def on_ready(self, **kwargs):
        """ 기능 준비 문맥 """
        pass
    
    @abstractmethod
    def on_input(self, **kwargs):
        """ 기능 입력 문맥 """
        pass
    
    @abstractmethod
    def on_error(self, **kwargs):
        """ 기능 에러 문맥 """
        pass
    
    @abstractmethod
    def on_success(self, **kwargs):
        """ 기능 성공 문맥 """
        pass
    
    @abstractmethod
    def on_finish(self, **kwargs):
        """ 기능 종료 문맥 """
        pass
        