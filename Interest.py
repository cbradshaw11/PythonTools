# Calculate compound

initial_amount = 1000.0
num_years = 30
interest = 0.08
amountPerYear = 1000.0

total = 0.0
noInterestTotal = 0.0
forFunsies = initial_amount * interest
for i in range(1, num_years+1):
    total = total + amountPerYear
    total = total + total*interest
    noInterestTotal = noInterestTotal + amountPerYear
    forFunsies = forFunsies + forFunsies*interest
    print("Interest Total : " + str(total))
    print("No Interest Total : " + str(noInterestTotal))
    print("For Funsies : " + str(forFunsies))
