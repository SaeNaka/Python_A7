# 眠れない夜は・・・（その2）

import sys
args = sys.argv
num = int(args[1]) # 入力した整数

file_name = "./files/sheep.txt" # ファイルのパス

with open(file_name, mode="w", encoding="utf-8") as f:
    for n in range(1, num+1):
        f.write(f"ひつじが{n}匹") # 出力を書き込み
        f.write("\n") # 改行