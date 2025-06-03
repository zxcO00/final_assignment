
import pandas as pd
import numpy as np
from indicator_forKBar_short import KBar

def Change_Cycle(Date, cycle_duration, KBar_dic, product_name):
    KBar_obj = KBar(Date, cycle=cycle_duration)

    for i in range(len(KBar_dic['time'])):
        time = KBar_dic['time'][i]
        open_price = KBar_dic['open'][i]
        close_price = KBar_dic['close'][i]
        high_price = KBar_dic['high'][i]
        low_price = KBar_dic['low'][i]
        volume = KBar_dic['volume'][i]
        amount = KBar_dic['amount'][i]

        KBar_obj.AddPrice(time, open_price, close_price, low_price, high_price, volume, amount, product_name)

    # 形成 KBar 字典
    KBar_dic = {}
    KBar_dic['time'] = KBar_obj.TAKBar['time']
    KBar_dic['product'] = np.repeat(product_name, len(KBar_dic['time']))  # 修正此行
    KBar_dic['open'] = KBar_obj.TAKBar['open']
    KBar_dic['high'] = KBar_obj.TAKBar['high']
    KBar_dic['low'] = KBar_obj.TAKBar['low']
    KBar_dic['close'] = KBar_obj.TAKBar['close']
    KBar_dic['volume'] = KBar_obj.TAKBar['volume']
    KBar_dic['amount'] = KBar_obj.TAKBar['amount']

    return KBar_dic

# 模擬初始化使用方式
if __name__ == '__main__':
    # 測試資料結構格式
    df = pd.DataFrame({
        'time': pd.date_range(start='2024-01-01', periods=3, freq='T'),
        'open': [100, 102, 101],
        'close': [101, 103, 100],
        'high': [102, 104, 102],
        'low': [99, 101, 98],
        'volume': [200, 220, 210],
        'amount': [20000, 22000, 21000]
    })
    data_dict = df.to_dict(orient='list')
    out = Change_Cycle("2024-01-01", 1, data_dict, "TEST")
    print(out)
