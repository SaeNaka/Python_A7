from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    #税額条件
    if salary >= 1000000:
        tax = (salary - 1000000) * 0.2 + 1000000 * 0.1
    else:
        tax = salary * 0.1

    #税の四捨五入
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
    #支給額の計算
    allowance = salary - tax
    
    return tax, allowance