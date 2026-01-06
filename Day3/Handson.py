'''1.List Manipulation: '''
# ● Remove the duplicates from the list.
input_list=list(map(int,input("Enter the values separated by space:").split()))
set1=set(input_list)
list2=list(set1)
print(f"Remove the duplicate into list{list2}")

#  Sort the list in descending order.
input_list.sort(reverse=True)
print(f"descending order:",input_list)

##● Calculate the sum of all the elements in the list.
total=sum(input_list)
print(total)

'''2. Tuple Operations:'''
# Create a tuple containing the names of five countries. Write a Python program that performs the following operations:
my_tuple=("India","australia","Jermany","American","Londan")

#● Print the length of the tuple.
print(len(my_tuple))

#● Check if a given country is present in the tuple
if "India" in my_tuple:
    print("yes")

#  Create a new tuple by concatenating the original tuple with another tuple containing five more countries.
tuple2=("Indonesia","Belize","Costa Rica","Russia","Serbia")
print(my_tuple + tuple2)

# Extra: Try modifying the element at 2nd index. What is output and why. Discuss it
'''my_tuple[2]="japan"
print(my_tuple)'''

#error is 'tuple' object does not support item assignment because uple is immutable tuple is created not chnage the value


'''3 . Dictionary Manipulation:'''
stoke={
    "Apple":20,
    "Mango":90,
    "Orange":60
}
print(stoke)

# Add a new item to the stock
stoke['Kiwi']=50
print(stoke)

 #Update the quantity of an existing item.
stoke['Mango']=120
print(stoke)

# Remove an item from the stock.
print(stoke.pop('Mango'))

# Print the items in stock alphabetically sorted along with their quantities
for item,vale in sorted(stoke.items()):
    print(item, ":", vale)
    
''' 4. List Comprehensions:'''
# Write a Python program that generates a list of squares of even numbers between 1 and 20 using list comprehension
nums=[x for x in range(1,20) if x % 2 == 0]
print(nums)

''' 5. Dictionary Iteration '''
# Create a dictionary representing the population of five different cities. Write a Python program that prints the 
# city with the highest population along with its population.

population = {
    "Mumbai": 2041100,
    "Delhi": 16787941,
    "Bengaluru": 12425393,
    "Chennai": 11324069,
    "Kolkata": 14864919
}
city=max(population,key=population.get)

print("City with highest population:")
print(city, ":", population[city])

''' 6. Tuple Unpacking: '''
# Write a Python program that takes a tuple of three integers representing the sides of a triangle as input and determines 
# if it forms a valid triangle. If it does, print its type (equilateral, isosceles, or scalene).

sides = tuple(map(int, input("Enter three sides of the triangle: ").split()))
a,b,c=sides

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
    
    if a==b==c:
        print("Triangle is equilateral")
    elif a==b or b==c or c==a:
        print("Triangle is isosceles")
    else:
         print("Triangle is scalene")
else:
    print(" It is Not Valid Triangle")


''' 7. List Sorting:'''
# Write a Python program that takes a list of tuples, where each tuple contains a student's name and their score in a test. 
# Sort the list based on the scores in descending order and print the names of the top three students.
students = [
    ("Amit", 85),
    ("Neha", 92),
    ("Rahul", 78),
    ("Priya", 95),
    ("Anjali", 88)
]
sorted_student=sorted(students,key=lambda x:x[1],reverse=True)
print(sorted_student)
for x in range(3):
    print(sorted_student[x][0])
    
''' Dictionary Filtering:'''
prices = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 150,
    "Milk": 30,
    "Bread": 25
}
threshold=int(input("Enter the threshold value:"))
for item,price in prices.items():
    if price < threshold:
        print(item, ":", price)
        
        
'''  List Operations '''
#  Write a Python program that takes two lists of integers as input and performs the following operations
input_list1=list(map(int,input("Enter the values separated by space:").split()))
input_list2=list(map(int,input("Enter the values separated by space:").split()))

set1=set(input_list1)
set2=set(input_list2)

#● Find the intersection of the two lists (common elements).
common_element=list(set1 & set2)
print(common_element)

# ● Find the union of the two lists (all elements without duplicates).
union_element=list(set1 | set2)
print(union_element)

# ● Find the elements present in the first list but not in the second list.
difference_element=list(set1 - set2)
print(difference_element)


'''  Dictionary Sorting '''
# Write a Python program that takes a dictionary containing names as keys and their corresponding ages as values. 
# Sort the dictionary based on ages in ascending order and print the names of the oldest and youngest person

# Dictionary with names and ages
Dict = {'parth': 23, 'temp': 24, 'nikul': 18}

sored_dict=dict(sorted(Dict.items(),key=lambda x:x[1]))

for name,age in sored_dict.items():
    print( name, ":", age)

oldest_person=max(Dict,key=Dict.get)
youngest_person=min(Dict,key=Dict.get)

print("oldest_person:",oldest_person)
print("youngest_person", youngest_person)