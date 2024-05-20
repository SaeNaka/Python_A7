from datetime import date
from database_nakagawa import session
from tables_nakagawa import Holiday

#登録したデータの削除
result = session.query(Holiday).filter_by(holi_date = date(2024, 1, 1)).delete()

#登録内容のコミット
session.commit()