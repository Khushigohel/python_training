# 1.  Write a program that takes a number as input from the user and displays whether the number is even or odd
number=int(input("Enter the number:"))

if number % 2 == 0:
    print(f"number is Even : {number}")
else:
    print(f"number is Odd : {number}")
    
# 2. Write a program that takes a list of numbers as input from the user and displays the sum of all the even numbers in the list.
input_list=input("Enter the Number separated by spaces:" )
number=input_list.split()
even_sum=0

for num in number:
    num=int(num)
    if num % 2 ==0:
        even_sum += num
print("Sum of the even numver is :",even_sum)

# 3. Write a program that displays the numbers from 1 to 10 using a for loop. (try with single line)
value=[x for x in range(1,11)]
print(value)

# 4.  Write a program that takes a number as input from the user and displays the multiplication table of the 
# number using a while loop.
n=int(input("Enter the number:"))
i=1
while i <11:
    res=n*i
    print(n, "*" ,i , "=",res)
    i+=1

# 5. Write a program that takes a list of numbers as input from the user and displays only the odd numbers in the list using a for loop.
input_list=input("Enter the Number separated by spaces:" )
number=input_list.split()

for num in number:
    num=int(num)
    if num % 2 !=0:
        print(num)

# 6. Write a program that takes a number as input from the user and displays whether the number is prime or not using a try-except block.
number=int(input("Enter the number:"))
flag = False
try:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
except ValueError:
    print("Please enter a valid integer number!")