import os
import shutil

class FileManager:
    
    _index = 0
    _root = os.getcwd() + '/data/'
    
    @classmethod
    def get(cls, file):
        """ 파일의 데이터 가져오기 """
        if (os.path.isfile(FileManager._root + file) is True):
            f = open(FileManager._root + file, 'r')
            line = f.readline()
            f.close()
            return line
        else:
            return False
    
    @classmethod
    def upsert(cls, file, data):
        """ 파일 생성 또는 재작성 """
        if (os.path.isdir(FileManager._root) is False):
            os.mkdir(FileManager._root)
            
        f = open(FileManager._root + file, 'w')
        f.write(data)
        f.close()
        
        if (os.path.isfile(FileManager._root + file) is True):
            return True
        else:
            return False
        
    @classmethod
    def remove(cls, file):
        """ 파일 삭제 """
        if (os.path.isfile(FileManager._root + file) is True):
            os.remove(FileManager._root + file)
            return True
        else:
            return False
            
    @classmethod
    def reset(cls):
        """ 디렉토리 초기화 """
        shutil.rmtree(FileManager._root)