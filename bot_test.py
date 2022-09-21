from utils.signal import Signal
import time
from iqoptionapi.stable_api import IQ_Option
import logging

EMAIL = "los.napath@gmail.com"
PASS = "testbot123456"

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
global ins
ins = IQ_Option(EMAIL, PASS)
check, reason= ins.connect()#connect to iqoption
print("Finish Logging in...", check, reason)

MODE = "PRACTICE"
# MODE = "REAL"
ins.change_balance(MODE)
print("Current Mode =", MODE)
ini_balance = ins.get_balance()
print("<BEFORE> get balance =", ini_balance)
# print("get currency =", ins.get_currency())

def buy():
    Money=1
    ACTIVES="GBPUSD"
    ACTION="call"#or "put"
    expirations_mode=1

    check,id=ins.buy(Money,ACTIVES,ACTION,expirations_mode)
    if check:
        print("!buy!")
    else:
        print("buy fail")

def sell():
    Money=1
    ACTIVES="GBPUSD"
    ACTION="put"
    expirations_mode=1

    check,id=ins.buy(Money,ACTIVES,ACTION,expirations_mode)
    if check:
        print("!sell!")
    else:
        print("sell fail")


symbol="USDZAR"
screener="forex"
exchange="FX_IDC"

signal = Signal(15, 5)
c = 0
count_open_order = 0
while True:
    print("Start[{}]".format(c))

    # if (c == 0):
    #     buy()
        
    # print(signal.get_master_tf())
    # print()

    sum, ma, oscil = signal.getSignal_15m(symbol, screener, exchange)
    if (sum['RECOMMENDATION'][:6] == 'STRONG'):
        print("-------------- TF 15m ----------------")
        print(sum)
        print(ma)
        print(oscil)

        
        sum5, ma5, oscil5 = signal.getSignal_5m(symbol, screener, exchange)
        print("-------------- TF 5m ----------------")
        print(sum5)
        print(ma5)
        print(oscil5)

        print("---------------------- SUMMARY ------------------------")
        print(sum['RECOMMENDATION'], sum5['RECOMMENDATION'])

        if (
            (sum['RECOMMENDATION'][-3:] == sum5['RECOMMENDATION'] 
                or sum['RECOMMENDATION'] == sum5['RECOMMENDATION'])
            and (sum5['RECOMMENDATION'] == 'BUY' 
                    or sum5['RECOMMENDATION'] == 'STRONG_BUY')):
            buy()
            count_open_order += 1
        elif (
            (sum['RECOMMENDATION'][-3:] == sum5['RECOMMENDATION'] 
                or sum['RECOMMENDATION'] == sum5['RECOMMENDATION'])
            and (sum5['RECOMMENDATION'] == 'SELL' 
                    or sum5['RECOMMENDATION'] == 'STRONG_SELL')):
            sell()
            count_open_order += 1

        print("Total Match Found {}; Total Loops {};".format(count_open_order, c))
        print("Init Balance =", ini_balance)
        # if (sum5['RECOMMENDATION'][:6] == 'STRONG'):
        #     print("<<<<<<<<<<<<<<< MATCHED >>>>>>>>>>>>>>>>>>>>")
        #     count_open_order += 1
        #     print("Total Match Found {}; Total Loops {}".format(count_open_order, c))
        #     print("-------------- TF 5m ----------------")
        #     print(sum5)
        #     print(ma5)
        #     print(oscil5)
        print("------------------------------")
    else:
        print('No Signal Match')
        print(sum)
        print(ma)
        print(oscil)
        print("------------------------------")

    c += 1

    # sleep for 1 min
    time.sleep(60)
