import sys
args = sys.argv
#引数を変数に代入
cat_name = args[1]

class IntroFam:
    def __init__(self, cat_name):
        self.cat_name = cat_name
    
    def cat_out(self):
        catnametxt = "飼い猫の名前は、" + self.cat_name + "です"
        return catnametxt
    
catnametxt = IntroFam(cat_name)
    
print(catnametxt.cat_out())