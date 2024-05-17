import sys
from func_salary_yajima import calcsalary # 作成したモジュールを呼び出す

args = sys.argv

# 入力された人数分繰り返す
for i in range(1, len(args)):
    salary = int(args[i]) # 給与
    pay_amount, tax_amount = calcsalary(salary)
    print(f"給与:{salary}、支給額：{pay_amount}、税額：{tax_amount}")
