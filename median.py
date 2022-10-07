"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    
def mean(num1,num2):
    return (num1+num2)/2

numbers = sorted(numbers)
size = numbers.length()
if size %2 ==1:
    print(numbers[(size-1)/2])  
else:
    print(mean(numbers[(size/2)-1],numbers[(size/2)-2]))
    
#print(numbers)
