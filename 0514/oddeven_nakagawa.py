import sys
args = sys.argv
#引数を変数に代入
num = int(args[1])

#条件
if num % 2 == 0:
    print('偶数', end = "")
else:
    print('奇数', end = "")