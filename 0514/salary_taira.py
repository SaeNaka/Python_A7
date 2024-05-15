from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
salary = args[1]

if int(salary)<=1000000:
    tax= int(salary)*0.1
else:
    tax = (int(salary)-1000000)*0.2 + 100000
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

result = int(salary)-tax
print (f"支給額:{result}、税額:{tax}")
