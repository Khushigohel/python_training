#1. Write a program that defines a function to calculate the area of a rectangle. The function should take the length 
# and width of the rectangle as input parameters and return the area.

def rectangle(width,lenght):
    return width * lenght

lenght=int(input("Enter the length:"))
width=int(input("Enter the width:"))

area=rectangle(lenght,width)
print("area of rectangle:",area)

# 2 Write a program that defines a function to calculate the factorial of a number. The function should take a single input 
# parameter and return the factorial of that number.

def Factorial(num):
    fact=1
    for i in range(1,num + 1):
        fact = fact * i
    return fact

number=int(input("Enter the number:"))
factorial=Factorial(number)
print(f"Factorial is: {factorial}")

# 3. Write a program that defines a function to calculate the sum of a list of numbers. The function should take a list of 
# numbers as input and return the sum of those numbers.

def sum_list(number):
    total=0
    for num in number:
        total += num
    return total

values = list(map(int, input("Enter numbers separated by space: ").split()))
res=sum_list(values)
print(f"Total sum of the list is {res}")

# 4.Write a program that defines a function to calculate the nth Fibonacci number. The function should take a single input 
# parameter and return the nth Fibonacci number.
def Fibonacci_number(number):
    a,b=0,1
    for i in range(3,number + 1):
        c=a+b
        a=b
        b=c
    return c 
number=int(input("ENter the number:"))
print(f"The {number}th Fibonacci number is:", Fibonacci_number(number))
    

