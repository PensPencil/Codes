"""2.Write a Python function to Display Fibonacci Sequence using Recursion"""
def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n = int(input("Enter number of terms :"))
if(n<0):
    print("Invalid Input")
else:
    print("The fibonacci series upto {} terms is :".format(n))
    for i in range(n):
        print(fib(i),end = ' ')
