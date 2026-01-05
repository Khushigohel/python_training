######  datatype  #######

num=100
print(type(num))

num1=34.78
print(type(num1))

expression1=num * 3
print(type(expression1))

expression2= num + num1
print(type(expression2))


######## math function #########
print(round(2.1))
print(round(66.9))
print(abs(-11))


####### string ######
name="khushi"
print(type(name))

name1='''this is datatype of the string it check which ye of data can be store'''
print(type(name1))

##### string concat #####
str1="khushi"
str2="gohel"
print(str1 + ' ' +  str2)

##### type conversion ######
userName="john"
age=50
print(userName + age)   # it get the error can only concatenate str (not "int") to str

userName="john"
age=str(50)
print(userName + age)

