#The next project we will use to evaluate our knowledge on math operations is to build a BMI calculator
#BMI means body mass index which is the ratio of a person's weight to their height
#We will build a program that outputs a user's body mass index by collecting inputs of their weight and height
#Then we will divide the inputs based on the BMI formula and output the result
#The BMI formula is
#BMI = weight(kg) / height(m2)
#The BMI result should be printed as a whole number
#This means that after division of weight and height, we will get a floating point as the output
#We will now typecast the result to be an integer and then round it to the nearest whole number

#First we will import the math function so we can use it to approximate our BMI to a whole number

import math

#Then print the Welcome message for the program

print("Welcome to the BMI Calculator...")

#Ask the user to input their weight in kilograms. We will store this as a float so we can divide

user_weight_kg = float((input("Please eneter your weight in kg: ")))

#Ask the user to input their height in meters square, we are to square this later due to the BMI equation

user_height_m2 = float((input("Please enter your height in m2: ")))

#We calculate the BMI using the user's inputed weight and height
#Take note the height is to the power of two based on the BMI equation

BMI = (user_weight_kg / (user_height_m2 ** 2))

#We print the raw BMI value which is in floating point with decimals

print("Your Body Mass Index(BMI) is " + str(BMI) + "kg/m2")

#Then we round it up using the round function and display it as a whole number

print("It is approximately " + str(round(BMI)) + "kg/m2")