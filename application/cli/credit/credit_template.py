from .._common.template import Template
from system.io import IOManager

class CreditTemplate(Template):
    
    _data = {}
    
    def input_data(self, **kwargs):
        """ 데이터 추가 """
        key = '%s(%s)' % (kwargs['name'], kwargs['card_number'])
        value = '%s: $ %d' % (key, kwargs['balance'])
        
        self._data[key] = value
        
    def input_error(self, **kwargs):
        """ 데이터 추가 """
        key = '%s(%s)' % (kwargs['name'], kwargs['card_number'])
        value = '%s: Error' % (key)
        
        self._data[key] = value
        
    def output(self, is_display=True):
        """ 알파벳 순으로 정렬된 키&값 반환 """
        result = sorted(self._data.items())
        
        for k, v in result:
            IOManager.add_buffer(v)
        
        if (is_display == True):
            return IOManager.display_cli_output()
        else:
            return IOManager.get_buffer()