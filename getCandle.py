from iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime

def toDate(timestamp):
    return datetime.fromtimestamp(timestamp)


MODE = "PRACTICE"
EMAIL = "los.napath@gmail.com"
PASS = "testbot123456"

global ins
ins = IQ_Option(EMAIL, PASS)
check, reason= ins.connect()#connect to iqoption
print("Finish Logging in...", check, reason)


goal="GBPUSD"
print("get candles")
# print(ins.get_candles(goal,60,111,time.time()))

# NOTE ins.get_candles get NON-OTC one

candles = ins.get_candles(goal,60,100,time.time())
print(len(candles))
print(candles[-1]['at'])
# temp = datetime.fromtimestamp(int(candles[-1]['at']))

print(toDate(candles[-1]['from']), candles[-1])
print(toDate(candles[-2]['from']), candles[-2])
print(type(candles[-1]['at']), candles[-1]['at'])
# print(type(toDate(candles[-1]['at'])))
  

# dt_obj = datetime.fromtimestamp(1661695838000000000)
  
# print("date_time:",dt_obj)
# print("type of dt:",type(dt_obj))