from decimal import Decimal, ROUND_HALF_UP

# 「給与」を渡すと「支給額」、「税額」を戻り値として戻す関数
def calcsalary(salary):
    threshold = 1000000

    if salary <= threshold: # 給与が100万円以下なら
        tax_amount = salary * 0.1
    else: # 給与が100万円を超えたら
        tax_amount = threshold * 0.1 + (salary - threshold) * 0.2

    # 四捨五入
    tax_amount = Decimal(tax_amount).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    # 支給額=給与-税額
    pay_amount = salary - tax_amount 

    # 戻り値は「支給額」と「税額」
    return pay_amount, tax_amount