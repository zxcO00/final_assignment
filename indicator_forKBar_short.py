# 載入必要套件
import requests,datetime,os,time
import numpy as np
import matplotlib.dates as mdates
#from talib.abstract import *  # 載入技術指標函數

    
# 算K棒
class KBar():
    # 設定初始化變數
    def __init__(self,date,cycle = 1):
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
        self.TAKBar['time'] = np.array([])
        self.TAKBar['open'] = np.array([])
        self.TAKBar['high'] = np.array([])
        self.TAKBar['low'] = np.array([])
        self.TAKBar['close'] = np.array([])
        self.TAKBar['volume'] = np.array([])
        self.current = datetime.datetime.strptime(date + ' 00:00:00','%Y-%m-%d %H:%M:%S')
        self.cycle = datetime.timedelta(minutes = cycle)
    # 更新最新報價
    def AddPrice(self,time,open_price,close_price,low_price,high_price,volume,amount,prod):
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
    # 取開盤價
    def GetOpen(self):
        return self.TAKBar['open']
    # 取最高價
    def GetHigh(self):
        return self.TAKBar['high']
    # 取最低價
    def GetLow(self):
        return self.TAKBar['low']
    # 取收盤價
    def GetClose(self):
        return self.TAKBar['close']
    # 取成交量
    def GetVolume(self):
        return self.TAKBar['volume']
    # 取MA值(MA期數)
    # def GetMA(self,n,matype):
    #     return MA(self.TAKBar,n,matype)    
    # # 取SMA值(SMA期數)
    # def GetSMA(self,n):
    #     return SMA(self.TAKBar,n)
    # # 取WMA值(WMA期數)
    # def GetWMA(self,n):
    #     return WMA(self.TAKBar,n)
    # # 取EMA值(EMA期數)
    # def GetEMA(self,n):
    #     return EMA(self.TAKBar,n)    
    # # 取布林通道值(中線期數)
    # def GetBBands(self,n):
    #     return BBANDS(self.TAKBar,n)   ##BBANDS()函數有很多選項,此處只使用期數 n
    # # RSI(RSI期數)
    # def GetRSI(self,n):
    #     return RSI(self.TAKBar,n)
    # # 取KD值(RSV期數,K值期數,D值期數)
    # def GetKD(self,rsv,k,d):
    #     return STOCH(self.TAKBar,fastk_period = rsv,slowk_period = k,slowd_period = d)
    # # 取得威廉指標        
    # def GetWILLR(self,tp=14):  
    #     return WILLR(self.TAKBar, timeperiod=tp)
    # # 取得乖離率
    # def GetBIAS(self,tn=10):
    #     mavalue=MA(self.TAKBar,timeperiod=tn,matype=0)
    #     return (self.TAKBar['close']-mavalue)/mavalue
