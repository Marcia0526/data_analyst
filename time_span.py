from datetime import datetime
from dateutil import parser
import numpy as np
import pandas as pd
# print(datetime(year=2015, month=7, day=4))
# print(parser.parse('09/20/2020 9:09'))
# print(parser.parse('20/09/2020 9:09'))
# print(parser.parse('20/09/2020 9:09').strftime('%A'))

# print(np.array('2015-07-04', dtype=np.datetime64))
# print(np.array('2015-07-04', dtype=np.datetime64) + np.arange(12))
# print(np.datetime64('2015-07-04 09:00:01') + np.arange(12))

# print(pd.to_datetime('09/09/2021 09:09'))

# print(pd.to_datetime([datetime(2021, 9, 1), '1th of July, 2019', '2018-Jul-09', '07/07/2020', '09-08-2017', '20150506']))
print(pd.date_range('2021-08-01', '08/09/2021'))
print(pd.date_range('2021-01-01', periods=5, freq='H'))
print(pd.date_range('2021-01-01', periods=5, freq='M'))
print(pd.timedelta_range(0, periods=10, freq='H'))
