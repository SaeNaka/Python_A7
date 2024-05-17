import sys

#モジュールのインポート
import func_salary_ono

salary = sys.argv  # コマンドライン引数を格納したリストの取得
a = len(salary) # 引数の個数

#実行
for i in range(0, a):
    v = list(func_salary_ono.calcsalary(salary[i]))
    print("給与:" + str(salary[i]) + "、税額:" + str(int(v[0])) + "、支給額:" + str(int(v[1])))