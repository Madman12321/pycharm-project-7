startLocation = int(input("Enter starting location: "))
diceRoll = int(input("Enter dice roll: "))
endLocation = startLocation + diceRoll
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)
if endLocation > 27:
    iter(num)
print("Your ending location is:", endLocation)

# add your code here please
transactionAmount = input("Enter transaction amount: ")
amountPaid = input("Enter amount paid: ")
change = float(amountPaid) - float(transactionAmount)
twenty_dollars = change // 20

change = change % 20

ten_dollars = change // 10

change = change % 10

five_dollars = change // 5

change = change % 5

one_dollars = change // 1

change = change % 1

quarter_dollar = change // .25

change = change % .25

dime_dollar = change // .10

change = change % .10

nickel_dollar = change // .05

change = change % .05

penny_dollar = change // .01

change = change % .01

# Print the results

print(f"Your change is: ")

print(f"{twenty_dollars} twenty dollar bill(s)")

print(f"{ten_dollars} ten dollar bill(s)")

print(f"{five_dollars} five dollar bill(s)")

print(f"{one_dollars} one dollar bill(s)")

print(f"{quarter_dollar} quarter(s)")

print(f"{dime_dollar} dime(s)")

print(f"{nickel_dollar} nickel(s)")

print(f"{penny_dollar} penny(s)")


