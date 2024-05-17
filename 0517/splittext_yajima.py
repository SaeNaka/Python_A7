# 英文のn番目の単語は？

import sys

args = sys.argv
text = args[1] # 英文
num = int(args[2]) # 何単語目か

words = text.split(" ") # 英文をスペースで分割
print(words[num-1], end="") # 表示