from tradingview_ta import TA_Handler, Interval, Exchange
import time

class Signal:

    def __init__(self, master_tf, sub_tf):
        self.master_tf = master_tf
        self.sub_tf = sub_tf

    def get_master_tf(self):
        return self.master_tf

    def get_sub_tf(self):
        return self.sub_tf

    def getSignal_15m(self, symbol, screener, exchange):
        result = TA_Handler(
            symbol=symbol,
            screener=screener,
            exchange=exchange,
            interval=Interval.INTERVAL_15_MINUTES)

      # return <summary>, <ma>, <oscill> 
        return result.get_analysis().summary, result.get_analysis().moving_averages, result.get_analysis().oscillators

    def getSignal_5m(self, symbol, screener, exchange):
        result = TA_Handler(
                                symbol= symbol,
                                screener= screener,
                                exchange= exchange,
                                interval=Interval.INTERVAL_5_MINUTES)
        # return <summary>, <ma>, <oscill> 
        return result.get_analysis().summary, result.get_analysis().moving_averages, result.get_analysis().oscillators