import sys
import datetime
from datetime import date
from database_nakagawa import session
from tables_nakagawa import Holiday

args = sys.argv
#引数を変数に代入
date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

#平日の料金表
weekday = {'大人' : 2000, '子供' : 1200}
#土日の料金表
weekend = {'大人' : 2400, '子供' : 1500}

#日付の分解
#年
year = int(date[:4]) 
#月
if date[4] == '0':
    month = int(date[5])
else:
    month = int(date[4:5])
#日
day = int(date[-2:])

#曜日の算出
dt = datetime.date(year, month, day)
week = dt.weekday()

#データを取得する
holidaylist=session.query(Holiday).all()

#人数制限
if 0 <= adult_num <= 20 and  0 <= child_num <= 20:
    #土日の場合
    if week == 5 or week == 6:
        adult_price = weekend['大人'] * adult_num
        child_price = weekend['子供'] * child_num
    #平日の場合
    else:
        adult_price = weekday['大人'] * adult_num
        child_price = weekday['子供'] * child_num
        #祝日の場合
        for holiday in holidaylist:
            if dt == holiday.holi_date:
                adult_price = weekend['大人'] * adult_num
                child_price = weekend['子供'] * child_num
                break

total_price = adult_price + child_price
print(total_price, end = '')