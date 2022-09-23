#Project Details
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Note: for this exercise, the expectation is that you explicitly write out the year
#(and therefore be out of date the next year)
#Ask user for their name
name = input("What is your name? ")
#Ask user for their age
user_age = int(input("What is your age? "))
if user_age > 100:
    print("You are already more than a 100 years")

#Ask user for their birth year
user_birth_date = int(input("What year were you born? "))
#Ask the user what year it is today
current_year = int(input("What year is this? "))
#Determine how many years is left for the user to clock 100 years
#DO this by subtracting the current year of the user from the user birth year
#Then you subtract the result from 100
age_100_years = 100 - (current_year - user_birth_date)
#Then print out the user's name plus their age and tell them how many years it will take them to clock 100 years
#print("Hello " + name + "!" + " You are " + str(user_age) + " years old now. \n" + "You will be" + " 100 years old in " + str(age_100_years) + " years time!")

#Let's try this with f strings
print(f"Hello {name}! You are {user_age} yearls old now. \nYou will be 100 years old in {age_100_years} years time!")

