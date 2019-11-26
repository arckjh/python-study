from .._common.context import Context
from .credit_event import CreditEvent
from .credit_error import CreditError
from .credit_template import CreditTemplate

class CreditContext(Context):
    
    template = None
    
    def __init__(self):
        self.template = CreditTemplate()
    
    def run(self, cmd = ''):
        """ 명령을 적절한 컨텍스트 함수 호출 """
        
        param = {}
        event = None
        
        try:
            cmd = cmd.replace('\n', '')
            cmd = cmd.split(' ')
            
            if (cmd[0] == 'Add'):
                param['name'] = cmd[1]
                param['card_number'] = cmd[2]
                param['limit'] = int(cmd[3].replace('$', ''))
                param['template'] = self.template
                
                event = CreditEvent()
                event.on_ready(**param)
                if (CreditError.is_error() is False):
                    event.on_input(**param)
                if (CreditError.is_error() is False):
                    event.on_add(**param)
            
            elif (cmd[0] == 'Charge'):
                param['name'] = cmd[1]
                param['card_number'] = cmd[2]
                param['ammount'] = int(cmd[3].replace('$', ''))
                param['template'] = self.template
                
                event = CreditEvent()
                event.on_ready(**param)
                if (CreditError.is_error() is False):
                    event.on_input(**param)
                if (CreditError.is_error() is False):
                    event.on_charge(**param)
                
            elif (cmd[0] == 'Credit'):
                param['name'] = cmd[1]
                param['card_number'] = cmd[2]
                param['ammount'] = int(cmd[3].replace('$', ''))
                param['template'] = self.template
                
                event = CreditEvent()
                event.on_ready(**param)
                if (CreditError.is_error() is False):
                    event.on_input(**param)
                if (CreditError.is_error() is False):
                    event.on_credit(**param)
            
            else:
                raise IndexError
            
        except IndexError:
            event = CreditEvent()
            CreditError.register(CreditError.INPUT_ERROR_CODE, CreditError.INPUT_ERROR_MSG)
              
        if (CreditError.is_error() is True):
            event.on_error()
        else:
            event.on_success()
        
        event.on_finish()