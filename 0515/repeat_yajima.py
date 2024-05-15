# 永遠の足し算
import sys

args = sys.argv

# 引数の整数
input = int(args[1])

# 足し算の結果
add_result = 0
# 繰り返し
while True:
    if add_result == 100: # ちょうど100になった場合
        print("Just 100!", end="")
        break
    elif add_result > 100: # 100を超えた場合
        print("Over!", end="")
        break
    add_result += input