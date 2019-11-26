
from application.cli.credit.credit_context import CreditContext
from application.cli.credit.credit_error import CreditError
from application.cli.credit.credit_event import CreditEvent
from application.cli.credit.credit_template import CreditTemplate
from system.io import IOManager

class TestCredit():
    
    input = ""
    output = ""
    
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.input = []
        self.input.append("Add Jane 4111111111111111 $1000\n")
        self.input.append("Add Evan 5454545454545454 $3000\n")
        self.input.append("Add Daniel 1234567890123456 $2000\n")
        self.input.append("Charge Jane 4111111111111111 $500\n")
        self.input.append("Charge Jane 4111111111111111 $800\n")
        self.input.append("Charge Evan 5454545454545454 $7\n")
        self.input.append("Credit Evan 5454545454545454 $100\n")
        self.input.append("Credit Jane 4111111111111111 $800\n")
        self.input.append("Credit Daniel 1234567890123456 $200\n")
        
        self.output = []
        self.output.append("Daniel(1234567890123456): Error");
        self.output.append("Evan(5454545454545454): $ -93");
        self.output.append("Jane(4111111111111111): $ 500");
            
    def teardown_method(self, method):
        pass

    def test_application(self):
        context = CreditContext()
        for input in self.input:
            context.run(input)
        queue = context.template.output(False)
        
        result = []
        for msg in iter(queue.get, None):
            result.append(msg)

            if (queue.empty()):
                break
        
        assert self.output == result