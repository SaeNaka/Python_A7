import sys
args = sys.argv

ma_point = int(args[1])
ja_point = int(args[2])
en_point = int(args[3])

if ma_point >= 70 and ja_point >= 70 and en_point >= 70:
    print("合格", end="")
elif (ma_point + ja_point + en_point) >= 220:
    if ma_point >= 50 and ja_point >= 50 and en_point >= 50:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")