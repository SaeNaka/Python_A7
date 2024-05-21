# 水族館の来場者数を登録　未完成

import sys
import datetime

from database_yajima import session # 1. データベースへの接続
from tables_yajima import AttendNum # 2. テーブル定義


args = sys.argv
year, month, day = int(args[1][:4]), int(args[1][4:6]), int(args[1][6:8]) # 日付(YYYYMMDD)
input_date = datetime.date(year, month, day) # 日付をdate型に変換
adult_num = int(args[2]) # 大人の人数
child_num = int(args[3]) # 子供の人数


result = session.query(AttendNum).filter(AttendNum.entry_date == input_date).all()

if result: # 日付が登録されていたら
    attend = AttendNum(
        entry_date = input_date,
        seq = result[-1].seq+1, 
        adult = adult_num,
        child = child_num
    )
else: # 日付が登録されていなかったら
    attend = AttendNum(
        entry_date = input_date,
        seq = 1,
        adult = adult_num,
        child = child_num
    )
session.add(attend)
session.commit()

