# 載入必要套件
import requests, datetime, os, time
import numpy as np
import matplotlib.dates as mdates
# from talib.abstract import *  # 載入技術指標函數

# 算K棒
class KBar():
    # 設定初始化變數
    def __init__(self, date, cycle=1):
        # K棒的頻率(分鐘)
        self.TAKBar = {
            'time': [],
            'open': [],
            'close': [],
            'high': [],
            'low': [],
            'volume': [],
            'amount': [],
            'product': []
        }
        self.current = datetime.datetime.strptime(date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
        self.cycle = datetime.timedelta(minutes=cycle)

    # 更新最新報價
    def AddPrice(self, time, open_price, close_price, low_price, high_price, volume, amount, prod):
        if len(self.TAKBar['close']) == 0:
            self.TAKBar['time'].append(time)
            self.TAKBar['open'].append(open_price)
            self.TAKBar['close'].append(close_price)
            self.TAKBar['low'].append(low_price)
            self.TAKBar['high'].append(high_price)
            self.TAKBar['volume'].append(volume)
            self.TAKBar['amount'].append(amount)
            self.current = time
        elif time <= self.current:
            self.TAKBar['close'][-1] = close_price
            self.TAKBar['volume'][-1] += volume
            self.TAKBar['amount'][-1] += amount
            if low_price < self.TAKBar['low'][-1]:
                self.TAKBar['low'][-1] = low_price
            if high_price > self.TAKBar['high'][-1]:
                self.TAKBar['high'][-1] = high_price
        else:
            self.TAKBar['time'].append(time)
            self.TAKBar['open'].append(open_price)
            self.TAKBar['close'].append(close_price)
            self.TAKBar['low'].append(low_price)
            self.TAKBar['high'].append(high_price)
            self.TAKBar['volume'].append(volume)
            self.TAKBar['amount'].append(amount)
            self.current = time

    def GetTime(self):
        return self.TAKBar['time']

    def GetOpen(self):
        return self.TAKBar['open']

    def GetHigh(self):
        return self.TAKBar['high']

    def GetLow(self):
        return self.TAKBar['low']

    def GetClose(self):
        return self.TAKBar['close']

    def GetVolume(self):
        return self.TAKBar['volume']

    # 以下為技術指標函數，如有需要可取消註解
    # def GetMA(self,n,matype):
    #     return MA(self.TAKBar,n,matype)    
    # def GetSMA(self,n):
    #     return SMA(self.TAKBar,n)
    # def GetWMA(self,n):
    #     return WMA(self.TAKBar,n)
    # def GetEMA(self,n):
    #     return EMA(self.TAKBar,n)    
    # def GetBBands(self,n):
    #     return BBANDS(self.TAKBar,n)
    # def GetRSI(self,n):
    #     return RSI(self.TAKBar,n)
    # def GetKD(self,rsv,k,d):
    #     return STOCH(self.TAKBar,fastk_period = rsv,slowk_period = k,slowd_period = d)
    # def GetWILLR(self,tp=14):  
    #     return WILLR(self.TAKBar, timeperiod=tp)
    # def GetBIAS(self,tn=10):
    #     mavalue = MA(self.TAKBar,timeperiod=tn,matype=0)
    #     return (self.TAKBar['close'] - mavalue) / mavalue
