#Project One
#Band name generator
#We will create a program that produces a band name for our user

print("Welcome to the Band name generator")
#Ask for the user's city where they grew up in and store it in the variable city_name
city_name = input("What is the name of the city you grew up in? \n ")
#Ask for the user's pet name if they had a pet and store the input in the variable pet_name
pet_name = input("What is your pet name? \n")
#Print the name of their band using string concatenation
#print("The name of your band could be " + city_name + " " + pet_name)
#Let's use f strings
print(f"The name of your band could be {city_name} {pet_name}")
