import sys
args = sys.argv
#引数を変数に代入
num = args[1]
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')