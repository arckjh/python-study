class Application:
    
    _object = None
    _config = None
    
    def __init__(self, config):
        Application._config = config.__dict__
    
    @classmethod
    def create_object(cls, config):
        if (Application._object == None):
            Application._object = Application(config)
        
        return Application._object
    
    @classmethod
    def get_object(cls):
        return Application._object
        
    @classmethod
    def get_config(cls):
        return Application._config
        
    @classmethod
    def destroy_object(cls):
        del Application._object