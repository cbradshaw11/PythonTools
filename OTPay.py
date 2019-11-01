
########################################################
# Title: OTPay                                         #
# Purpose: This Script was written when                #
# the first 4 hours of overtime at Boeing              #
# were unpaid. The purpose was to determine            #
# the average hourly pay for overtime work.            #
# Usage: OTPay.py [YearlySalary] [YearlyNumberofHours] #
########################################################

import sys

#Default yearly salary amount is 70,000 dollars
#Default yearly number of hours is 2,040 hours
Salary = 70000
NumHours = 2040
Hourly = Salary/NumHours

def OTPAY():
	ot = int(input("ENTER OT HOURS: "))
	hourspaidOT = ot-4
	otpay = hourspaidOT*(Hourly+5)
	revisedhourly = otpay/ot
	
	print("\nAmount per hour if you work "+str(ot)+" hours of OT is: $"+str(revisedhourly))
	print("Compared to the normal hourly rate of: $"+str(Hourly))
	print("Total amount of money earned from working this overtime is: $"+str(otpay))
	
if __name__ == '__main__' :
	if(len(sys.argv) == 2):
		Salary = sys.argv[1]
	if(len(sys.argv) > 2):
		NumHours = sys.argv[2]
	Hourly = Salary/NumHours
	OTPAY()