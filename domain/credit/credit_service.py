from .credit_entity import CreditEntity

class CreditService:
    
    def issue_new_card(self, card_number, name, limit):
        """ 신규 카드 발급 """
        entity = CreditEntity(card_number, name)
        return entity.create_account(limit)
        
    def increase_balance(self, card_number, name, money):
        """ 잔액 증가 """
        entity = CreditEntity(card_number, name)
        return entity.update_balance(money)
    
    def decrease_balance(self, card_number, name, money):
        """ 잔액 감소 """
        entity = CreditEntity(card_number, name)
        return entity.update_balance(money * -1)
    
    def get_account_status(self, card_number, name):
        """ 계좌 상태 반환 """
        entity = CreditEntity(card_number, name)
        return entity.get_account()