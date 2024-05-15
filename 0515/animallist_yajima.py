# リストを操作して出力

import sys

# 引数
args = sys.argv
input_index = int(args[1])
input_animal = args[2]

# 動物の名前リスト
animallist = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 1.
animallist.insert(input_index, input_animal)

# 2.
animallist.pop()

# 3.
animallist.sort()
print(animallist, end="")


