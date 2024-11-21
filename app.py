from config import *
from model.DatabaseUtil import *
from model.DataAPI import *
from time import sleep, time
from model.RusalApiDataSender import *
   
   
def workThread(afterLoopWaitTime:float = 1.):
    '''
        asking database for data to send for consumer
        if data finishes in the table goes to another one add try to find data in it
        if go thrue the table has finished it waits for 3 second before start the new loop 
    '''
    while True:         
        y, m, id = DataAPI.getLastSent()
        data, y, m = DataAPI.getNewValue(y,m,id)
        
        if data:
            dataSendRes = RusalApiDataSender.sendScanerData(*data)
            if dataSendRes:
                res = DataAPI.setLastSent(y, m, data[0])
                if not res:
                    print('write ti file error')
        else:
            break
    sleep(afterLoopWaitTime)
    
    
if __name__ == "__main__":
    prevTime = time()
    while True:
        nowTime = time()
        if nowTime - prevTime > status_send_interval:
            res = RusalApiDataSender.sendStatus(1)
            if res:
                prevTime = nowTime
        workThread()
    
    # while True:
    #     y, m, id = DataAPI.getLastSent()
    #     data, y, m = DataAPI.getNewValue(y,m,id)
        
    #     if data:
    #         print('data to sent:', data, y, m)
    #         res = DataAPI.setLastSent(y, m, data[0])
    #         print('is set', res, 'new last got data is:',   DataAPI.getLastSent())
    #     else:
    #         break
    #     sleep(0.5)