from introduce_yajima import Intro
import sys

args = sys.argv
name = args[1]
age = args[2]

intro = Intro(name, age)
nametxt = intro.name_out()
agetxt = intro.age_out()

print(nametxt)
print(agetxt)