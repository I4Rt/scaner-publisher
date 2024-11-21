from config import *
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
class RusalApiDataSender:
    __headers  = outer_headers
    __user     = user_name
    __password = user_password
    
    __dataSendRoute   = 'https://echo.free.beeceptor.com/scanerData' # TODO: change it
    __statusSendRoute = 'https://echo.free.beeceptor.com/statusData' # TODO: change it
    
    @classmethod
    def sendScanerData(cls, id:int, weight:float, andodeClass:int, size:int, date:str) -> bool:
        data = {
                "id": id,
                "time": datetime.strptime(date, '%H:%M:%S %d.%m.%Y').strftime('%Y-%m-%d %H:%M:%S'),            # “yyyy-MM-dd HH:mm:ss”
                "weight": weight,                                                # значения в килограммах
                "class": andodeClass,                                            # 0 … 5
                "type": size,                                                    # 0 - короткий анод, 1 - длинный анод
                }
        resp = requests.post(cls.__dataSendRoute, 
                                 auth=HTTPBasicAuth(cls.__user, cls.__password), 
                                 headers=cls.__headers, 
                                 json=data, 
                                 verify=False
                                )
        if resp.status_code == 200: 
            print('\n\n\ntext', resp.text)
        
            respBody = resp.json()
            if respBody:
                if 'error' in respBody:
                    return False
        return True
    
    @classmethod
    def sendStatus(cls, status:int) -> bool:
        data =  {"status": status} # 1 - работа, 2 - запрет
                
        resp = requests.post(cls.__statusSendRoute, 
                                 auth=HTTPBasicAuth(cls.__user, cls.__password), 
                                 headers=cls.__headers, 
                                 json=data, 
                                 verify=False
                                )
        print('\n\n\ntext', resp.text)
        
        if resp.status_code == 200: 
            print('\n\n\ntext', resp.text)
            respBody = resp.json()
            if respBody:
                if 'error' in respBody:
                    return False
        return True