# 新幹線の駅間の計算

import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv
eki1 = args[1]
eki2 = args[2]

distance_dict = {"東京": 0.00,
                 "品川": 6.78,
                 "新横浜": 25.54,
                 "名古屋": 342.02,
                 "京都": 476.31,
                 "新大阪": 515.35}

try:
    if distance_dict[eki1]<distance_dict[eki2]:
        distance = distance_dict[eki2]-distance_dict[eki1]
    else:
        distance = distance_dict[eki1]-distance_dict[eki2]


    print(round(distance, 2), end="")
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")