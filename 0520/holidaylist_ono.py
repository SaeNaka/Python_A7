from database_ono import session
from tables_ono import Holiday

holidaylist = session.query(Holiday).all()

for Holiday in holidaylist:
    print(Holiday.holi_date,Holiday.holi_text)