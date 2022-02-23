
def ReadConfig():
	global COST_OF_BUYING_ASSET
	global INITIAL_CAPITAL
	global USDT_AMOUNT
	global AMOUNT_BORROWED

	f = open("margin.cfg", "r")
	line = f.readline()
	while(line):
		if("buy_price" in line):
			newline = line.split(":")[1].replace(" ", "")
			COST_OF_BUYING_ASSET = float(newline)
		if("account_value" in line):
			newline = line.split(":")[1].replace(" ", "")
			INITIAL_CAPITAL = float(newline)
		if("usdt" in line):
			newline = line.split(":")[1].replace(" ", "")
			USDT_AMOUNT = float(newline)
		if("borrow" in line):
			newline = line.split(":")[1].replace(" ", "")
			AMOUNT_BORROWED = float(newline)
		line = f.readline()

ReadConfig()

#USDT_AMOUNT = 5150.9
#INITIAL_CAPITAL = 5264.6
POSSIBLE_AMOUNT = INITIAL_CAPITAL * 9.

#AMOUNT_BORROWED = 40000.

MARGIN_PERCENT = AMOUNT_BORROWED/POSSIBLE_AMOUNT

USED_MARGIN = INITIAL_CAPITAL * MARGIN_PERCENT

ACCOUNT_VALUE = INITIAL_CAPITAL + AMOUNT_BORROWED

DEBT_RATIO = AMOUNT_BORROWED / ACCOUNT_VALUE
DEBT_RATIO_PERCENT = DEBT_RATIO * 100.

print("Current debt ratio : " + str(DEBT_RATIO_PERCENT) + "%")

#COST_OF_BUYING_ASSET = 27.60
AMOUNT_SPENT = USDT_AMOUNT + AMOUNT_BORROWED
AMOUNT_ASSET_BOUGHT = AMOUNT_SPENT / COST_OF_BUYING_ASSET

MAX_DEBT_RATIO = 0.97

LOWEST_ACCOUNT_VALUE = AMOUNT_BORROWED / MAX_DEBT_RATIO

AMOUNT_NOT_SPENT = INITIAL_CAPITAL - USDT_AMOUNT

LOWEST_PRICE = (LOWEST_ACCOUNT_VALUE - AMOUNT_NOT_SPENT) / AMOUNT_ASSET_BOUGHT

print("Lowest price before liquidation : $" + str(LOWEST_PRICE)) 

