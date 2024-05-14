# 奇数・偶数判定
import sys
input = int(sys.argv[1])

if input%2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")
