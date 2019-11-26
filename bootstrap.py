import argparse
import time
import sys
from config import init_app

if (__name__ == '__main__'):
    
    # 멀티 테넌시 & 환경 옵션
    mode = 'cli'
    env = 'dev'
    
    # 어플리케이션 객체 로드 및 실행
    init_app(env, mode)