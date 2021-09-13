
#let's use some comments.

#Loan details here:

money_owed = float(input("How many Pirate Doubloons do you owe?\n"))
apr = float(input("What is your annual percentage rate?\n")) 
payment = float(input("How much is your monthly payment, in Doubloons?\n"))
months = int(input("How many months would you like to see results for?\n"))


# Divide apr by 100 to get a percentage, then divide by 12 to get monthly payments
monthly_rate = apr/100/12


for i in range(months):

    # add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    # Making payments
    money_owed = money_owed - payment

    # Print the results
    print("Paid", payment, "of which", interest_paid, "was interest;", end=' ')
    print("Now I owe", money_owed)
