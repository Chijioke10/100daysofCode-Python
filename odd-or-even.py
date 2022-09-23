#In this code challenge, we're going to be creating a program that determines whether a number is odd or even

#We will ask the user to input a number and we will determine if that number is even or odd

#We cannot do this without using the modulo operator which is the % symbol

#The modulo operator tells us the remainder when two number divides

#For example 4 modulo (%) 2 is the same thing as 4 / 2

#The result is 2 without any remainders, so 4 % 2 = 0

#The modulo only prints out the remainder of the equation

#We know that even numbers are numbers that can be divided by 2 without a remainder

#So 2, 4, 6, 8, 10, etc are all even numbers because they can be divided by 2 without a remainder

#While numbers like 3, 5, 7, 9, 11, etc are all odd numbers

#With this knowledge we can use the if statements to know that
#If a number the user inputs can be divided without remainder, it is an even number
#Or else, if the number is divided by 2 with a remainder, it is odd

#First we ask the user to input any number to check if it is even or odd
number = int(input("Input any number to check if it is even or odd: "))

#Then we check to know if the number is odd or even

#We do this by using an if statements that check if the number inputted by the user can be divided by 2 without remainder
if number % 2 == 0:
    print(f"The number {number} is an even number!")
else:
    print(f"The number {number} is an odd number!")
