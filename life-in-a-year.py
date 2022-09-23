#We are going to create a life in a year program
#This program will ask the user for their age
#Then it will print out how many days, weeks, and months they have before they turn 90 years old.
#Keep it in mind that there are 365 days in a year
#52 weeks in a year
#And 12 months in a year

#Ask the user for their age
age = (input("What is your current age?: "))

#Change the age variable to an integer so we can perform math on it
age = int(age)

#The age in days will be 90 years multiplied by 365 days to give us the total days in 90 years
#Then we get the amount of days the user has lived till now
#We get this by multiplying the age variable by 365
#Then we subtract the two results to get the remaining age in days
age_in_days = (90 * 365) - (age * 365)

#Next we get age in weeks
#We do this by multiplying 90 years by 52 weeks just like we did with age in days
#Then multiply the user's current age by 52 weeks
#Then we subract both values
age_in_weeks = (90 * 52) - (age * 52)

#Repeat the same step for months
age_in_months = (90 * 12) - (age * 12)

print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")