import sys
args = sys.argv
#引数を変数に代入
name = args[1]
age = args[2]

import introduce_ono

myself = introduce_ono.Intro(name,age)

print(myself.name_out())
print(myself.age_out())