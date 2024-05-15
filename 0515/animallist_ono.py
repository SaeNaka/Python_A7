import sys
args = sys.argv
#引数を変数に代入
i = int(args[1])
animal = args[2]
#動物の名前リストを定義
animallist = ["giraffe", "tiger", "zebra", "elephant", "lion"]
# 第2引数で設定したインデックスの位置に第3引数の動物名を挿入
animallist.insert(i,animal)
# リストの最後の要素を削除
del animallist[-1]
# リストを昇順に並び替え
animallist.sort()
#出力
print(animallist)