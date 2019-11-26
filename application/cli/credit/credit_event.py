from luhn import verify
from domain.credit.credit_service import CreditService
from .._common.event import Event
from .credit_error import CreditError

class CreditEvent(Event):
    
    def on_ready(self, **kwargs):
        """ 기능 준비 문맥 """
        pass
    
    def on_input(self, **kwargs):
        """ 신용 카드 번호 체크 이벤트 """
        if (verify(kwargs['card_number']) == False):
            CreditError.register( \
                CreditError.CARD_NUMBER_ERROR_CODE, \
                CreditError.CARD_NUMBER_ERROR_MSG)
            kwargs['template'].input_error(**kwargs)
    
    def on_add(self, **kwargs):
        """ 새로운 신용카드 발급 이벤트 """
        service = CreditService()
        if (service.issue_new_card( kwargs['card_number'], kwargs['name'], kwargs['limit']) == False):
            CreditError.register( \
                CreditError.CARD_ADD_ERROR_CODE, \
                CreditError.CARD_ADD_ERROR_MSG)
            kwargs['template'].input_error(**kwargs)
        else:
            result = service.get_account_status(kwargs['card_number'], kwargs['name'])
            kwargs['balance'] = result['balance']
            kwargs['template'].input_data(**kwargs)
    
    def on_charge(self, **kwargs):
        """ 잔액 증가 이벤트 """
        service = CreditService()
        if (service.increase_balance(kwargs['card_number'], kwargs['name'], kwargs['ammount']) == False):
            CreditError.register( \
                CreditError.CARD_CHARGE_ERROR_CODE, \
                CreditError.CARD_CHARGE_ERROR_MSG)
            kwargs['template'].input_error(**kwargs)
        else:
            result = service.get_account_status(kwargs['card_number'], kwargs['name'])
            kwargs['balance'] = result['balance']
            kwargs['template'].input_data(**kwargs)
            
    def on_credit(self, **kwargs):
        """ 잔액 감소 이벤트 """
        service = CreditService()
        if (service.decrease_balance(kwargs['card_number'], kwargs['name'], kwargs['ammount']) == False):
            CreditError.register( \
                CreditError.CARD_CREDIT_ERROR_CODE, \
                CreditError.CARD_CREDIT_ERROR_MSG)
            kwargs['template'].input_error(**kwargs)
        else:
            result = service.get_account_status(kwargs['card_number'], kwargs['name'])
            kwargs['balance'] = result['balance']
            kwargs['template'].input_data(**kwargs)
    
    def on_error(self, **kwargs):
        """ 기능 에러 문맥 """
        #error = CreditError.get()
        pass
    
    def on_success(self, **kwargs):
        """ 기능 성공 문맥 """
        pass
    
    def on_finish(self, **kwargs):
        """ 기능 종료 문맥 """
        CreditError.clear()
        