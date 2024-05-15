import sys
args = sys.argv
#引数を変数に代入
num = int(args[1])
sum = 0

while True:
    sum = sum + num
    if sum >= 100:
        break

if sum == 100:print("Just 100!")
if sum > 100:print("Over!")