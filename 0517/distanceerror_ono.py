import sys
args = sys.argv
#引数を変数に代入
station1 = args[1]
station2 = args[2]
#辞書を定義
records = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪":515.35
}
#実行
try:
    print(abs(round(records[station2] - records[station1],2)))
except:
    print("のぞみの停車駅を引数に設定してください")