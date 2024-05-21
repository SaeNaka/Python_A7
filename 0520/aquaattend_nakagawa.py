import sys
import datetime
from datetime import date
from database_nakagawa import session
from tables_nakagawa import Attendnum

args = sys.argv
#引数を変数に代入
date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

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

#date型に変更
dt = datetime.date(year, month, day)

#登録するデータの編集
attendnum = Attendnum(
    date = dt,
    seq = 1,
    adult = adult_num,
    child = child_num
)

#連番処理
if dt == attendnum.date: 
    #日付が同じ場合の一番最後のものを取得
    aqualist = session.query(Attendnum).filter_by(date = dt).all()
    attendnum = Attendnum(
        date = dt,
        #取得したaqualistのseqに1追加
        seq =  len(aqualist) + 1,
        adult = adult_num,
        child = child_num
        )

#Insert処理
session.add(attendnum)
#登録内容のコミット
session.commit()