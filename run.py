from utils.signal import Signal
import time

symbol="GBPUSD"
screener="forex"
exchange="FX_IDC"

signal = Signal(15, 5)
c = 0
count_open_order = 0
while True:
    print("Start[{}]".format(c))
    print("------------------------------")
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
        if (sum5['RECOMMENDATION'][:6] == 'STRONG'):
            print("<<<<<<<<<<<<<<< MATCHED >>>>>>>>>>>>>>>>>>>>")
            count_open_order += 1
            print("Total Match Found {}; Total Loops {}".format(count_open_order, c))
        #     print("-------------- TF 5m ----------------")
        #     print(sum5)
        #     print(ma5)
        #     print(oscil5)


    c += 1

    time.sleep(30)
