import sys
args = sys.argv
salary = int(args[1])

#モジュールのインポート
import func_salary_ono

#実行
v = list(func_salary_ono.calcsalary(salary))
print("給与:" + str(salary) + "、税額:" + str(int(v[0])) + "、支給額:" + str(int(v[1])))