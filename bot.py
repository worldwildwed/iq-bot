import time
from iqoptionapi.stable_api import IQ_Option
import logging
from utils.signal import Signal
import time


EMAIL = "los.napath@gmail.com"
PASS = "testbot123456"

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
ins = IQ_Option(EMAIL, PASS)
check, reason= ins.connect()#connect to iqoption
print("Finish Logging in...", check, reason)
# print(type(ins), dir(ins))

# # print("iq-options modules:")
# # for i in dir(ins):
# #     print(" >", i)

# # print("-------------------------")

MODE = "PRACTICE"
# MODE = "REAL"
ins.change_balance(MODE)
print("Current Mode =", MODE)
print("get balance =", ins.get_balance())
print("get currency =", ins.get_currency())

goal="GBPUSD"
print("get candles")
# print(ins.get_candles(goal,60,111,time.time()))

candles = ins.get_candles(goal,60,10,time.time())
print(type(candles), len(candles))
print(candles[0])
print(candles[-1])

# Money=1
# ACTIVES="GBPUSD"
# ACTION="call"#or "put"
# expirations_mode=1

# check,id=ins.buy(Money,ACTIVES,ACTION,expirations_mode)
# if check:
#     print("!buy!")
# else:
#     print("buy fail")


# OPEN SELL #
# Money=1
# ACTIVES="GBPUSD"
# ACTION="put"
# expirations_mode=1

# check,id=ins.buy(Money,ACTIVES,ACTION,expirations_mode)
# if check:
#     print("!sell!")
# else:
#     print("sell fail")

