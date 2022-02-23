initial_salary = 82500
annualSalaryIncrease = 0.03
annualContribution = .08

amount = 0.0
current_salary = initial_salary
for i in range(25, 66):
    print(i)
    current_salary = current_salary  + current_salary*annualSalaryIncrease
    print("current salary = " + str(current_salary))
    contribution = current_salary * annualContribution
    print("401k contribution = " + str(contribution))
