import datetime
import sys
args=sys.argv

input1=args[1]
input2=int(args[2])
input3=int(args[3])

yyyy=int(input1[0:4])
mm=int(input1[4:6])
dd=int(input1[6:8])

dt = datetime.datetime(yyyy,mm,dd)
if dt.weekday() == 5 or dt.weekday() == 6:
    sum = (2400*input2) + (1500*input3)
else:
    sum = (2000*input2) + (1200*input3)

print(sum,end="")
