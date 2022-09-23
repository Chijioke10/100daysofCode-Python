#In this code challenge, we're going to create an upgraded version of our BMI calculator

#In the previous BMI calculator, we just collected the user's weight and height and divided it and printed a BMI value

#In this upgraded version, we're going to use the BMI result of the user to tell them their weight status
#I.e if they're underweight, overweight, obese, etc

#Remember the BMI = weight (kg) / height (m2)

#Note,
# A BMI of under 18.5 is underweight
# A BMI of over 18.5 but under 25 is a normal weight
# A BMI of over 25 but under 30 is overweight
# A BMI of over 30 but under 35 is obese
# A BMI of over 35 is clinically obesed

#So we're going to take the input of our user in kg and m, for weight and height and get the result of their BMI
#Then we will use our knowledge of if statements to print out their BMI

#Note that If statements and elifs work in ascending order

#We have to code it from smallest to largest

#Note, you should round the BMI to the nearest whole number

#Let's go

print("Welcome to the Upgraded BMI Calculator 2.0")

weight = float(input("What is your weight in kg?: "))

height = float(input("What is your height in m2?: "))

BMI = round(weight / height ** 2)

#Now to check for our user BMI result

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight!")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight!")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight!")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese!")
else:
    print(f"Your BMI is {BMI}, you are clinically obese!")

print("Thank you for using our upgraded BMI calculator, hope you enjoyed it!")
