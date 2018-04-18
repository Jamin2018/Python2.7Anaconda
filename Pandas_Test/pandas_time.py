# -*- coding: utf-8 -*-
import pandas as pd
from pandas.tseries.offsets import Day
from datetime import datetime
csv1 = pd.read_csv('0211-0225bak.csv')

# time = datetime(2018-02-26-04-24-45)
# print(time)
# csv1['settlement-end-date'] = pd.Series(pd.to_datetime(csv1['settlement-end-date']))

t1 = csv1['posted-date'].to_frame().iloc[1333,0]
t2 = csv1['posted-date'].to_frame().iloc[3110,0]

# print(csv1['posted-date'].sort_values(ascending=True).head(5))
# print(csv[csv['posted-date']>t].head(11))