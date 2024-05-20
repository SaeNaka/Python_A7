import sys
#パッケージをインポート
import qrcode
import os

args = sys.argv
#引数を変数に代入
input_url = args[1]
input_file = args[2]

#QRコードを生成
img = qrcode.make(input_url)
#ファイルに保存
img.save(os.path.join('..', 'files', input_file))
