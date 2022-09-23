#In this project, we will create a program that displays the amount to be paid after purchasing something
#The program would ask the user how much the total bill is
#It will ask them how much they would like to tip their waiter, it must be a 10, 12 or 15% tip
#It will ask them how many people would be splitting the bill
#Then it will display the total bill to be shared per person

import math

print("Welcome to the tip calculator!")

#Ask for the bill for their purchase
initial_bill = float(input("What is your total bill in $?: $"))

#Ask them how much tip they will like to pay, the tip should be in percentages of 10, 12 or 15
tip = int(input("What percentage of tip do you want to give? 10, 12, or 15: "))

#Ask them how many people are going to split the bill
users_number_split_bill = int(input("How many people are splitting the bill?: "))

#Calculate the percentage of the tip
#We calculate this by dividing the tip value of 10, 12 or 15 by 100 and multiplying it by the initial bill

tip = ((tip / 100) * initial_bill)

#Next we will need to get the value of our bill plus our tip to get the total bill
#We do this by adding the initial pill plus the tip

bill_plus_tip = initial_bill + tip

#Next we will get the amount to be paid by each user who is splitting the bill
#We do this by dividing the total bill plus tip variable by the number of users splitting the bill

split_bill_amount = round(bill_plus_tip / users_number_split_bill, 2)

#Note we used the round function to round up the total billing amount to two decimal places

#Then we print how much each person should pay
print(f"Each person should pay: ${split_bill_amount}")




