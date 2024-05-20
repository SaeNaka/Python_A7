from introduce_nakagawa import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name

#飼い猫の名前を表示するメソッド
    def cat_out(self):
        catnametext = f"飼い猫の名前は、{self.cat_name}です"
        return catnametext