# Congratulations, you've got a job at Python Pizza.
#
# Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.

# Small Pizza: $15
#
# Medium Pizza: $20
#
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
#
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1


# 🚨 Don't change the code below 👇

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

small_pizza_price = 15

medium_pizza_price = 20

large_pizza_price = 25

pepperoni_small_pizza_price = 2

pepperoni_medium_and_large_price = 3

extra_chesse_for_all_pizza = 1

if size == "S":
    bill += small_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_small_pizza_price
    if extra_cheese == "Y":
        bill += extra_chesse_for_all_pizza
    print(f"Your total bill is ${bill}")
elif size == "M":
    bill += medium_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_medium_and_large_price
    if extra_cheese == "Y":
        bill += extra_chesse_for_all_pizza
    print(f"Your total bill is ${bill}")
elif size == "L":
    bill += large_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_medium_and_large_price
    if extra_cheese == "Y":
        bill += extra_chesse_for_all_pizza
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, your order is invalid, please input a valid order")



