import sys
import os
args = sys.argv
#引数を変数に代入
input = int(args[1])

with open(os.path.join('..', 'files', 'sheep.txt'), mode = 'w', encoding = 'utf-8') as f:
    for i in range(1, input + 1):
        f.write('ひつじが' + str(i) + '匹\n' )