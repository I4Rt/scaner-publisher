import json
from tools.TableNameAssist import *
class FileStorageUtil:
    __filePath = 'data/last_sent_info.txt'
    
    @classmethod
    def writeInfo(cls, Y:int, M:int, ID:int) -> bool:
        try:
            with open(cls.__filePath, 'w') as file:
                file.write(json.dumps([Y, M, ID]))
                return True
        except Exception as e:
            print(e)
            return False
        
    @classmethod
    def readInfo(cls) -> tuple[int|None, int|None, int|None]:
        '''
        returns: year, month, id
        '''
        try:
            with open(cls.__filePath, 'r') as file:
                data = file.read()
                arr = json.loads(data)
                return tuple(arr)
        except:
            return (None, None, None)
            
