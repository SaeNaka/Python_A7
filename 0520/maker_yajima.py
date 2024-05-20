# パッケージをインポート
import qrcode
import sys
import os

args = sys.argv
qr_url = args[1] # QRコードを作成するURL
file_name = args[2] # QRコードのPNGファイル名


# QRコードを生成
img = qrcode.make(qr_url)

# ファイルに保存
path = os.path.join("./", "files", file_name)
img.save(path)


# 実行例
# python ./0520/maker_yajima.py https://job.mynavi.jp/2025/ mynavi_qr_yajima.png
