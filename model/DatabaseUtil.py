from tools.DBSessionMaker import *
from tools.TableNameAssist import *
from model.FileStorageUtil import *
from functools import cmp_to_key

class DatabaseUtil:
    
    @staticmethod
    def getLastNotSentMeasurement(year, month, id, limit = 1):
        '''
            returns: [id, weight, class, size]
        '''
        with DBSessionMaker.getSession() as ses:
            if id == None:
                id = 0
                
            FileStorageUtil.readInfo()
            sqlQuery = f'select id, weight, class, size, date from Scanner_results_{month}_{year} where id > {id} order by id limit {limit};'
            res = ses.execute(text(sqlQuery))
            
            data = list(map( lambda row: row[:], res))
            return data
        
    @staticmethod 
    def getFirstTable(greaterThan=None):
        with DBSessionMaker.getSession() as ses:
            sqlQuery = f'SELECT name FROM sqlite_master WHERE type="table";'
            res = ses.execute(text(sqlQuery))
        
            names = [name for name in map( lambda row: row[0], res) if 'Scanner_results' in name ]
            smallest = 'Scanner_results_99_9999' # maximal table name
        
            for name in names:
                if greaterThan:
                    if TableNameAssist.tableOneIsGreaterOrEqualThanTableTwo(greaterThan, name):
                        continue
                if TableNameAssist.tableOneIsGreaterOrEqualThanTableTwo(smallest, name):
                    smallest = name
            if smallest != 'Scanner_results_99_9999':
                return smallest
            return None


