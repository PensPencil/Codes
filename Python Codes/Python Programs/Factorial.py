#Set-4
"""1.Write a Python function to Find Factorial of Number using Recursion. The function accepts
the number as an argument."""
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter an Integer :"))
if(n<0):
    print("Invalid Input")
    exit()
print("The factorial of {} is :{}".format(n,fact(n)))