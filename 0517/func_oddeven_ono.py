import sys
args = sys.argv
num1 = int(args[1])
num2 = int(args[2])
num3 = int(args[3])

def calcvalue(a):
    oddeven = " "
    if a % 2 == 0:
        oddeven = "偶数"
    else:
        oddeven = "奇数"
    return oddeven

# 実行
print(str(num1) + 'は' + calcvalue(num1))
print(str(num2) + 'は' + calcvalue(num2))
print(str(num3) + 'は' + calcvalue(num3))