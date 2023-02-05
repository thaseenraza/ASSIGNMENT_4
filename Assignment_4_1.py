# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35

num = int(input("Enter the Number to which 25 is to be added : "))
funct = lambda x : x+25
result = funct(num)
print("The Output for the given Input  is : " , result)
