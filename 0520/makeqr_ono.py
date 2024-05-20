import sys
args = sys.argv
#引数を変数に代入
url = args[1]
file_name = args[2]

import qrcode
img = qrcode.make(url)

import os
path = os.path.join("..", "0520", file_name + ".png")

img.save(path)