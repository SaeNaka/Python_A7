import sys
#モジュールを取り込む
from func_salary_nakagawa import calcsalary
args = sys.argv

#複数人の処理
for i in range(1, len(args)):
    #引数を変数に代入
    salary = int(args[i])
    tax, allowance = calcsalary(salary)
    print(f'給与:{salary}、支給額:{allowance}、税額:{tax}')