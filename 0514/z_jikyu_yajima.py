# 時給計算プログラム
# 時給の入力
jikyu = int(input("時給はいくらですか？"))

# 時間の入力
jikan = int(input("何時間働きましたか？"))

# 計算
kyuryou = jikyu * jikan

# 結果を表示
print(f"時給{jikyu}円で、{jikan}時間働いたので、、、\n給料は{kyuryou}円です。")