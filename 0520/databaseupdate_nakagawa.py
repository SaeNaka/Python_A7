from datetime import date
from database_nakagawa import session
from tables_nakagawa import Holiday

#登録したデータの取得
holiday = session.query(Holiday).filter_by(holi_date = date(2024, 1, 1)).first()

#更新するデータの更新
holiday.holi_text = 'お正月'
#Update処理
session.add(holiday)
#登録内容のコミット
session.commit()