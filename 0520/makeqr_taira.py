import sys
import qrcode
import os

args = sys.argv

input1 = args[1]
input2 = args[2]

img = qrcode.make(input1)

path = os.path.join(f"..","files","{input2}")
img.save(path)
