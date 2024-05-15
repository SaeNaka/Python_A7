import sys
args = sys.argv

input1 = args[1]
input2 = args[2]
input3 = args[3]

if int(input1)>=50 and int(input2)>=50 and int(input3)>=50:
    if (int(input1)>=70 and int(input2)>=70 and int(input3)>=70) or (int(input1)+int(input2)+int(input3) >= 220) :
        print("合格")
    else:
        print("不合格")
else:
    print("不合格")

