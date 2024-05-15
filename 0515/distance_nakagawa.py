import sys
args = sys.argv
#引数を変数に代入
station_start = args[1]
station_last = args[2]

#辞書を作成
distances = {
    '東京': 0.00, '品川': 6.78,  '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35
}

#引数間の距離の計算
distance = abs(distances[station_last] - distances[station_start])
#小数点第二位で四捨五入
distance = round(distance, 2)

print(distance, end = '')