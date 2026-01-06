# 1. Write a program that takes two numbers as input from the user and displays their sum.
n1 = int(input("Enter the number1:"))
n2= int(input("Enter the number2:"))

ans=n1 + n2 
print("sum f two number is:",ans)

#2. Write a program that takes a string as input from the user and displays it in uppercase letters.
input_str=input("Enter the String:")
print("String  is:",input_str.upper())

# 3. Write a program that displays the following text, using triple quotes: Programming is fun. I love Python.
text='''Programming is fun. 
I love Python.'''
print(text)

# 4.  Write a program that displays the following text, using escape characters:She said, "Hello, world!"
print("She said, \"Hello, world!\"")

# 5.  Write a program that takes a sentence as input from the user and displays the number of words in the sentence.
text=input("Enter the text")
count_txt=len(text.split())
print(count_txt)
