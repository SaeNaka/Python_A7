import sys
#モジュールを取り込む
from introduce_nakagawa import Intro

args = sys.argv
#引数を変数に代入
input_name = args[1]
input_age = args[2]

#インスタンスを作成
person = Intro(input_name, input_age)
#インポートした値を代入
nametxt = person.name_out()
agetxt = person.age_out()

print(nametxt)
print(agetxt)