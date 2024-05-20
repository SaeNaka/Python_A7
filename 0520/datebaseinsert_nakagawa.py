from datetime import date
from database_nakagawa import session
from tables_nakagawa import Holiday

#登録するデータの編集
holiday = Holiday(
    holi_date = date(2024, 1, 1), 
    holi_text = 'お正月'
)

#Insert処理
session.add(holiday)
#登録内容のコミット
session.commit()