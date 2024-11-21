from model.FileStorageUtil import *
from model.DatabaseUtil import *
from tools.TableNameAssist import *


class DataAPI:
    
    @staticmethod            
    def getLastSent() -> tuple[str, str, int] | None:
        '''
            returns: y, m, id
        '''
        y, m, id = FileStorageUtil.readInfo()
        
        if y and m and id:
            return y, m, id
        
        tableName = DatabaseUtil.getFirstTable()
        if tableName:
            y, m = TableNameAssist.pullYearMonthFromTablename(tableName)
            return y, m, None
        return None
    
    @staticmethod
    def getNewValue(y, m, id):
        nextTable = f'Scanner_results_{m}_{y}'
        res = DatabaseUtil.getLastNotSentMeasurement(y, m, id)
        while len(res) == 0:
            id = None
            nextTable = DatabaseUtil.getFirstTable(greaterThan=nextTable)
            
            if nextTable is None:
                break
            y, m = TableNameAssist.pullYearMonthFromTablename(nextTable)
            res = DatabaseUtil.getLastNotSentMeasurement(y, m, id)
            print(nextTable, res)
        if nextTable:
            return res[0], y, m
        return None, y, m
                
    
    @staticmethod
    def setLastSent(y, m, id):
        return FileStorageUtil.writeInfo(y, m, id)
        
        