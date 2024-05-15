import sys
args = sys.argv
#引数を変数に代入
sum = int(args[1])

add = 0

while True:
    if add == 100:
        print('Just 100!', end = '')
        break
    elif add > 100:
         print('Over!', end = '')
         break
    add += sum