# 給与の支払い額
import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv
# 引数の給与
salary = int(args[1])
# 閾値100万円
threshold = 1000000

if salary <= threshold: # 給与が100万円以下なら
    tax_amount = salary * 0.1
else: # 給与が100万円を超えたら
    tax_amount = threshold * 0.1 + (salary - threshold) * 0.2

# 四捨五入
tax_amount = Decimal(tax_amount).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

# 支給額=給与-税額
pay_amount = salary - tax_amount 

# 結果
print(f"支給額:{pay_amount}、税額:{tax_amount}", end="")