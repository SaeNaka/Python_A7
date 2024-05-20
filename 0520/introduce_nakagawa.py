class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#名前を表示するメソッド
    def name_out(self):
        nametxt = f"私の名前は、{self.name}です"
        return nametxt
#年齢を表示するメソッド
    def age_out(self):
        agetxt = f"年齢は、{self.age}歳です"
        return agetxt