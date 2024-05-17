# 素因数分解

import sys
args = sys.argv
num = int(args[1]) # 整数

target = num
results = []

for i in range(2, num):
    # i(=2,3,・・・num-1)で割り切れたらリストに追加
    while target % i == 0:
        results.append(i)
        target /= i

print(results, end="")
