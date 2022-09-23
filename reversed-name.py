#We will create a program that asks the user for their first name and last name
#Then we will print out their full name by combining their first and last name to be a full name
#Then we will print out their full name
#Then we will reverse their name and print it out
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + " " + last_name
print(full_name)
reversed_name = full_name[::-1]
print(reversed_name)