# 水族館の入園料

import sys
import datetime

args = sys.argv
year, month, day = int(args[1][:4]), int(args[1][4:6]), int(args[1][6:8]) # 日付(YYYYMMDD)
adult_num = int(args[2]) # 大人の人数
child_num = int(args[3]) # 子供の人数

# 料金表
weekday_price = {"adult": 2000, "child": 1200}
weekend_price = {"adult": 2400, "child": 1500}

# 曜日判定
dt = datetime.datetime(year, month, day)

if dt.weekday() < 5: # 平日のとき
    total = weekday_price["adult"]*adult_num + weekday_price["child"]*child_num
else: # 土日のとき
    total = weekend_price["adult"]*adult_num + weekend_price["child"]*child_num

# 出力
print(total, end="")
