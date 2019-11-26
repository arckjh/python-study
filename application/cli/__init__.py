from .credit.credit_context import CreditContext
from .credit.credit_template import CreditTemplate
from system.io import IOManager
from system.file import FileManager
from system.application import Application

def main():
    """ 파일 표준 입력 & 어플리케이션 기능 라우팅 """
    FileManager.reset()
    
    config = Application.get_config()
    
    if (config['UNITTEST'] is False):
        input_list = IOManager.get_file_input()
        context = CreditContext()
        for input in input_list:
            context.run(input)
        context.template.output()
        
    else:
        pass