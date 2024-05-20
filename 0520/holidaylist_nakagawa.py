from database_nakagawa import session
from tables_nakagawa import Holiday

# データを取得する
holidaylist=session.query(Holiday).all()

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)