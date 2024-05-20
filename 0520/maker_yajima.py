# パッケージをインポート
import qrcode
import sys

args = sys.argv
qr_url = args[1] # QRコードを作成するURL
file_path = args[2] # QRコードのPNGファイルのパス


# QRコードを生成
img = qrcode.make(qr_url)

# ファイルに保存
img.save(file_path)


# 実行例
# python ./0520/maker_yajima.py https://job.mynavi.jp/2025/ ./files/mynavi_qr_yajima.png
