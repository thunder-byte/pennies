money = input("Enter the amount of money: ")
money = int(money)
dollars = money // 100
cents = money % 100
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
cents = cents % 5
pennies = cents
print(dollars, "dollars,", quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", pennies, "pennies")

dollars = money // 100
quarters = (money % 100) // 25
dimes = ((money % 100) % 25) // 10
nickels = (((money % 100) % 25) % 10) // 5
pennies = ((((money % 100) % 25) % 10) % 5)
print(dollars, "dollars,", quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", pennies, "pennies")