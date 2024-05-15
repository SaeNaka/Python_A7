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

if distance_dict[eki1]<distance_dict[eki2]:
    distance = distance_dict[eki2]-distance_dict[eki1]
else:
    distance = distance_dict[eki1]-distance_dict[eki2]

# 四捨五入
# distance = Decimal(str(distance)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# print(f"{distance:.2f}")
print(round(distance, 2))
