#四捨五入のためにモジュールをインポート
from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
#引数を変数に代入
salary = int(args[1])
# 税額の計算
if salary <= 1000000:
    tax = salary * 0.1
else:
    salary_plus = salary - 1000000
    tax = (salary_plus * 0.2) + (1000000 * 0.1)
tax = Decimal(tax).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
# 支給額の計算
pay = salary - tax
print("支給額:" + str(pay) + "、税額:" + str(tax))