import sys
args = sys.argv
#引数を変数に代入
text = args[1].split()
num = int(args[2])

print(text[num - 1])