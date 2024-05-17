from func_salary_taira import calcsalary
import sys
args = sys.argv
input1 = int(args[1])
input2 = int(args[2])
input3 = int(args[3])

a=(input1,input2,input3)

for i in a:
    salary = i
    pay1,tax1 = calcsalary(salary) 
    print(f"給与：{salary}、支給額：{pay1}、税額：{tax1}")
