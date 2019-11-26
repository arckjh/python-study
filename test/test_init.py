import argparse
import time
import sys
import os

# 멀티 테넌시 & 환경 옵션
mode = 'cli'
env = 'dev'
unittest = True

import sys, os
cur_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, cur_path + '/../')

# 어플리케이션 객체 로드 및 실행
from config import init_app
init_app(env, mode, unittest)