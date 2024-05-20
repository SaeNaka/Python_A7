import sys
#モジュールを取り込む
from introduce_nakagawa import Intro
from introfamily_nakagawa import IntroFam

args = sys.argv
#引数を変数に代入
input_name = args[1]
input_age = args[2]
input_cat_name = args[3]

#インスタンスを作成
introduce = IntroFam(input_name, input_age, input_cat_name)
#インポートした値を代入
nametxt = introduce.name_out()
agetxt = introduce.age_out()
cattet = introduce.cat_out()

print(nametxt)
print(agetxt)
print(cattet)