import os
# 1.  Write a program that opens a text file and reads the contents of the file.
file=open('Day7/file.txt','r')
read_file=file.read()
print(read_file)

# 2.  Write a program that opens a text file and writes some text to the file.
file_write=open('Day7/file.txt','w')
write=file_write.write("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.It syntax is easy to write and understand")
print("Data write Sucessfully....")

# 3. Write a program that opens a binary file and reads the first 10 bytes of the file
file=open('Day7/file_binary.bin','rb')
read_file_binary=file.read(10)
print(read_file_binary)

# 4.  Write a program that creates a new text file, writes some text to the file, and then renames the file.
import os

file = open("Day7/file1.txt", "x")
file.write("It is my new txt file that I am using for my Python task.")
file.close()

print("Data added successfully.")

os.rename("Day7/file1.txt", "Day7/new_file_task.txt")
print("File renamed successfully.")

# 5.  Write a program that deletes a text file
os.remove('Day7/python.txt')
print("File sucessfully Delete..")
