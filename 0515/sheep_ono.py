import sys
args = sys.argv
#引数を変数に代入
n = int(args[1])
for i in range(1, n + 1, 1):
    print("ひつじが" + str(i) + "匹")