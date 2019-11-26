import os
from datetime import timedelta
from importlib import import_module
from system.application import Application

class Config:
    VERSION = '1.0'
    TIMEZONE = 'Asia/Seoul'
    BASEPATH = os.path.abspath(os.path.dirname(__file__))
    APPPATH = ''
    SECRET_KEY = 'M2WaS7VgE9GQDO0e'
    UNITTEST = False
    
class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    
class TestConfig(Config):
    ENV = 'test'
    DEBUG = True

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    
def init_app(env, mode, unittest = False):
    """ 어플리케이션 생성 함수 """
    config = None
    
    if (env == 'dev'):
        config = DevConfig
    elif (env == 'test'):
        config = TestConfig
    elif (env == 'prod'):
        config = ProdConfig
    else:
        os.sys.exit('Envrionment is wrong.')
    
    if (mode != 'cli'):
        os.sys.exit('Mode is wrong.')
    
    config.UNITTEST = unittest
    
    Application.create_object(config);
    
    config.APPPATH = config.BASEPATH + '/application/' + mode
    module = import_module('.' + mode, package='application')
    module.main()