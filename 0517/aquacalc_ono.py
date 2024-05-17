import sys
args = sys.argv
date = str(args[1])
adults = int(args[2])
children = int(args[3])

y = date[0:4]
m = date[4:6]
d = date[6:8]

import calendar
weekday = calendar.weekday(int(y), int(m), int(d))

if weekday >= 0 and weekday <= 4:
    fee = (adults * 2000) + (children * 1200)
else:
    fee = (adults * 2400) + (children * 1500)
print(fee)