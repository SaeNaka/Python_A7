import sys
args = sys.argv
#引数を変数に代入
sentence = args[1] 
num = int(args[2])

#文字の分割
words = sentence.split(' ') 
print(words[num - 1], end = '')