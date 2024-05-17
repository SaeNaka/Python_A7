#四捨五入のためにモジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

#関数
def calcsalary(salary):
    if salary <= 1000000:
        tax = salary * 0.1
    else:
        salary_plus = salary - 1000000
        tax = (salary_plus * 0.2) + (1000000 * 0.1)
        tax = Decimal(tax).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
    pay = salary - tax
    return tax, pay