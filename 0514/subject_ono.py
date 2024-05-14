import sys
args = sys.argv
#引数を変数に代入
Math = int(args[1])
Japanese = int(args[2])
English = int(args[3])
sum = Math + Japanese + English
if (Math >= 70 and Japanese >= 70 and English >= 70) or sum >= 220:
    if Math > 50 and Japanese > 50 and English > 50:
        print("合格")
    else:
        pass
else:
    print("不合格")
    