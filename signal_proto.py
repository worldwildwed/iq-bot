from tradingview_ta import TA_Handler, Interval, Exchange
import time

# tesla = TA_Handler(
#     symbol="TSLA",
#     screener="america",
#     exchange="NASDAQ",
#     interval=Interval.INTERVAL_1_DAY
# )
# print(tesla.get_analysis().summary)


# signal = TA_Handler(
#     symbol="EURUSD",
#     screener="forex",
#     exchange="FX_IDC",
#     interval=Interval.INTERVAL_15_MINUTES
# )
# print(signal.get_analysis().summary)
# print(signal.get_analysis().oscillators)
# print(signal.get_analysis().moving_averages)

# print(type(TA_Handler))
# print(dir(TA_Handler))
# print(TA_Handler.symbol)

count = 0
signal_15 = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_15_MINUTES
    )
print("Get Signal 15m")
print(signal_15.get_analysis().oscillators)
print(signal_15.get_analysis().summary)
print(signal_15.get_analysis().moving_averages)
    
while count < 3:

    signal_5 = TA_Handler(
        symbol="EURUSD",
        screener="forex",
        exchange="FX_IDC",
        interval=Interval.INTERVAL_5_MINUTES
    )

    print("Get Signal of", count+1)
    print(signal_5.get_analysis().oscillators)
    print(signal_5.get_analysis().summary)
    print(signal_5.get_analysis().moving_averages)
    
    # sleep for 5 mins
    time.sleep(60*5)
    count += 1
