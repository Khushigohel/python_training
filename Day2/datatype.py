#assignments task perform

# 1.Create a variable called "age" and assign it the value 25.
age=22

# 2. Create a variable called "name" and assign it your name as a string.
name="Khushi Gohel"

# 3. Create a variable called "temperature" and assign it a float value representing the current temperature in degrees Celsius.
temperature=27.0

# 4. Calculate the area of a rectangle with length 5 and width 10, and assign the result to a variable called "area".
lenght=5
widht=10
area=widht * lenght
print(area)

# 5.incremnt adge by 1  compound assignment operator.
age+=1
print(age)

# 6.  Create function in python which take integer as input and convert it to binary string 
#with the bin built in function
def convertBinary(num):
    return bin(num)[2:]

num=int(input("Enter the interger number:"))
print("binary number is :"+ convertBinary(num))

# convert the without built in function
def binary(n):
    if n == 0:
        return "0"
    if n == 1:
         return "1"
    return binary(n // 2)  + str(n % 2)

num=int(input("Enter the interger number:"))
print("binary number is :"+ binary(num))
