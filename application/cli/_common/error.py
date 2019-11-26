from abc import *

class Error(metaclass=ABCMeta): 
    
    _code = 0
    _msg = ''
    
    @classmethod
    def is_error(cls):
        if (Error._code == 0):
            return False
        else:
            return True
    
    @classmethod
    def get(cls):
        result = {}
        result['code'] = Error._code
        result['msg'] = Error._msg
        
        return result

    @classmethod
    def register(cls, code, msg):
        Error._code = code;
        Error._msg = msg;

    @classmethod
    def clear(cls):
        Error._code = 0;
        Error._msg = '';