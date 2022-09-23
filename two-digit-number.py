#Exercise
#Write a program that adds the digits in a two digit number.
# E.g If the input was 35, the output should be 3 + 5 = 8
#First ask the user to input a two digit number

two_digit_num = (input("Input a two digit number: "))

#The two digit numbers are stored as strings
#We need to extract the individual digits using subscripting
#Subscript the first digit of the two digit number by using the index zero

first_digit = int(two_digit_num[0])

#You will type cast it to an integer for further math operations
#Subscript the second digit of the two digit number by using index one

second_digit = int(two_digit_num[1])

#Also typecast it to an int for math operations

#Since both first and second digit are now integers, we can add them now
#We add them and assign them to a variable "result"

result = first_digit + second_digit

#We print the result

print(result)

