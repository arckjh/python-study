from system.file import FileManager

class CreditFileRepo:
    
    @classmethod
    def select(cls, key):
        """ 데이터 가져옴 """
        return FileManager.get(key)
    
    @classmethod
    def insert(cls, key, value):
        """ 데이터 저장 """
        return FileManager.upsert(key, value)
    
    @classmethod
    def update(cls, key, value):
        """ 데이터 업데이트 """
        return FileManager.upsert(key, value)
    
    @classmethod
    def delete(cls, key):
        """ 데이터 삭제 """
        return FileManager.remove(key)
    