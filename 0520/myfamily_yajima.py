from introfamily_yajima import IntroFam
import sys

args = sys.argv
name = args[1]
age = args[2]
cat_name = args[3]

introfam = IntroFam(name, age, cat_name)


nametxt = introfam.name_out()
agetxt = introfam.age_out()
cattxt = introfam.cat_out()

print(nametxt)
print(agetxt)
print(cattxt)