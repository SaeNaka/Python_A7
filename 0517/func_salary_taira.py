from decimal import Decimal, ROUND_HALF_UP
def calcsalary(salary):
    if int(salary)<=1000000:
        tax= int(salary)*0.1
    else:
        tax = (int(salary)-1000000)*0.2 + 100000
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    pay = int(salary)-tax

    return pay,tax


