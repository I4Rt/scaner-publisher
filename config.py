from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base, declared_attr
import base64

Base = declarative_base()

DATABASE_NAME = 'C:\\Users\\Марков Владимир\\sqlite_dbases\\test.db'
e = create_engine(f'sqlite:///{DATABASE_NAME}', echo=False)


user_name     = 'ask_rusal_scaner'
user_password = 'qwerty'

outer_headers = {'content-type': 'application/json',
                 'Host': 'echo.free.beeceptor.com',
                 #'Authorization': f'Base {base64.b64encode(user_name+':'+user_password)}',
                 'accept': '*/*'
                }

status_send_interval = 10