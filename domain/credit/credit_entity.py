import json
import hashlib
from infra.credit_file_repo import CreditFileRepo

class CreditEntity:
    
    _key = ''
    _card_number = ''
    _name = ''
    _balance = 0
    _limit = 0
    
    def __init__(self, card_number, name):
        """ 엔티티 생성 """
        sha = hashlib.new('md5')
        sha.update((card_number + name).encode('utf-8'))
        key = sha.hexdigest()
        
        self._key = key
        self._card_number = card_number
        self._name = name
        
        json_value = CreditFileRepo.select(self._key)
        try:
            account = json.loads(json_value)
            self._balance = account['balance']
            self._limit = account['limit']
        except TypeError:
            self._balance = 0
            self._limit = 0
        
    def create_account(self, limit):
        """ 계좌 생성하기 """
        self._limit = limit
        
        param = {}
        param['card_number'] = self._card_number
        param['name'] = self._name
        param['balance'] = self._balance
        param['limit'] = self._limit
        value = json.dumps(param)
        
        return CreditFileRepo.insert(self._key, value)
    
    def update_balance(self, money):
        """ 잔액 업데이트 """
        
        ## 잔액 증가            
        if (money > 0):
            self._balance += money
            
            param = {}
            param['card_number'] = self._card_number
            param['name'] = self._name
            param['balance'] = self._balance
            param['limit'] = self._limit
            value = json.dumps(param)
                
            return CreditFileRepo.update(self._key, value)
        
        ## 잔액 감소            
        elif (money < 0):
            
            ## 소비 한도 허용
            if (self._limit + money >= 0):
                self._balance += money
                
                param = {}
                param['card_number'] = self._card_number
                param['name'] = self._name
                param['balance'] = self._balance
                param['limit'] = self._limit
                value = json.dumps(param)
                
                return CreditFileRepo.update(self._key, value)
                
            ## 소비 한도 비허용
            else:
                return False
        
        ## 잔액 변동 없음
        else:
            return True
    
    def get_account(self):
        """ 계좌정보 가져오기 """
        json_value = CreditFileRepo.select(self._key)
        try:
            return json.loads(json_value)
        except TypeError:
            return False