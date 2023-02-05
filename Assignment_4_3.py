# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]



lst = [4, 5, 2, 9]
def square(lst):
    return lst ** 2

data = list(map(square,lst))
print("The Squares of the Given list is : ",data)
