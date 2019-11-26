import sys
import queue
import fileinput

class IOManager():
    
    _buffer = queue.Queue()
    
    @classmethod
    def get_file_input(cls):
        """ 파일 입력값 반환 """
        input = []
        
        for line in fileinput.input():
            input.append(line)
            
        return input
    
    @classmethod
    def get_cli_input(cls, **kwargs):
        """ 커맨드 라인 입력값 반환 """
        i = 0;
        for k, v in kwargs.items():
            try:
                print(sys.argv[i])
                kwargs[k] = sys.argv[i]
            except IndexError:
                kwargs[k] = None
            i += 1
            
        return kwargs
    
    @classmethod
    def add_buffer(cls, msg):
        """ 버퍼 추가 """
        IOManager._buffer.put(msg);
        
    @classmethod
    def remove_buffer(cls):
        """ 버퍼 삭제 """
        IOManager._buffer.get();
        
    @classmethod
    def get_buffer(cls):
        """ 버퍼 반환 """
        return IOManager._buffer
        
    @classmethod
    def display_cli_output(cls):
        """ 커맨드 라인 버퍼 출력 """
        for msg in iter(IOManager._buffer.get, None):
            print(msg)
            
            if (IOManager._buffer.empty()):
                break