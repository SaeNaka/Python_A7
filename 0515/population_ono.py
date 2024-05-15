import sys
args = sys.argv
#引数を変数に代入
i = int(args[1])
#世界人口ランキングを定義
popu_tuple=("China", "India", "U.S.A", "Indonesia", "Pakistan", 
            "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
#タプルをリストに変換
popu_tuple = list(popu_tuple)
#引数に指定した順位の国名を出力
print(popu_tuple[i - 1])