import sys
args = sys.argv
#引数を変数に代入
input1 = int(args[1])
input2 = args[2]

animallist = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#第2引数で設定したインデックスの位置に、第3引数の動物名を挿入する
animallist.insert(input1,input2)

#リストの最後の要素を削除する
animallist.pop()

#リストを昇順に並べ替える
animallist.sort()

print(animallist, end = '')