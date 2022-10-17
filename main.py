#Shortcut to comment lines
# command + / in mac
# ctrl + / in windows

# #Print Function will print to output here its console
# print('jawahar reddy')

# #Input function
# x = input('Enter your name:')
# print('Hello, ' + x)

# #Fundatemental data types
# # int
# #Float

# #Type function will give Data type of the result after doing math
# print(type(5+3.5))

# #This will give Remainder
# print(33%2)
# print(type(0.0))
# print(3//4)
# #This will give value before decimal in quotient
# print(type(3//4))
# print(50//100)
# #This will give complete value in quotient
# print(50/100)
# print(type(50//100))
# print(type(50/100))

# print(12.5*3)
# #This will give 2 power 3 (** - Power of function)
# print(2**3)

# #Math Functions
# print(round(45.678))

# #bin function is used to convert to binary representation of a given integer in the bracets
# #0b1001 -> 0b indicates its a binary number
# y = bin(9)
# print(y)
# # here we are telling in bracets that hey here y is binary number with base as 2 , and python interpretor will  convert to integer
# print(int(y,2))

# "Formated strings "
var1 = 'jawahar'
var2 = 31
print(f'hi {var1} you are {var2} years old')
# for i in [1, 2, 3, 4, 5, 6]:
#     for x in ['a', 'b', 'c', 'd', 'e', 'f']:
#         print(i, x)

# for item in [1,2,3,4,5]:
#   print(item)
#   print(item)
#   print(item)
# print(item) #this print is out of loop but item value hold value of last iteration i.e 5 so it printed 5

# iterables -> list,dictionary,tuple,set,string,Range  are the ONLY ones in python which can be looped ( like an internal table)
# user = {
#   'name': 'Jawahar',
#   'age': '31',
#   'swim': 'yes'
# }
# for item in user.items(): # This will print  as tuple both key value pair
#   print(item)
# for key , value in user.items():
#   print(key,value)

# for item in user.values(): # This will print only value
#   print(item)
# for item in user.keys(): # This will print only keys
#   print(item)

#Excercise
# my_list = [1,2,3,4,5,6,7,8,9,10]
# cnt = 0
# for x in my_list:
#   cnt = cnt + x
# print(cnt) #indentation is very imp here.if print statement is jus below cnt line then it will print a different output .
#here by putting print statemet exactly below of for statement then it will print last iteration value

#Ranges
# for i in range(1,100): # this will print nubers from 1 to 99
#   print(i)
# for _ in range(2): #here _ is dummy variable declaration to print list from range
#   print(list(range(0,11)))

# #Enumurate
# for i,char in enumerate(list(range(0,10))):
#   if i == 5 :
#     print(f"we are in index = {i}")

#   print(i,char)

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
#in python indentation means code blocks are very important
for list in picture:
    for i in list:
        if (i == 0):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("")  #This print will print empty string to next line

#Excersice to print duplicates in a given list

# some_list = ['a','b','c','b','d','c','d','a','e']
# some_list.sort()
# duplicate_list = []


# print(some_list)
# for value in some_list:
#  if some_list.count(value) > 1:
#    if value not in duplicate_list:
#     duplicate_list.append(value)
# print(duplicate_list)
# Function example
def total(num1, num2):
    return (num1 + num2)


sum = total(10, 5)
print(total(sum, 5))

#Excerise -Tesla self driving car
# def checkDriverAge(age=0):
#     return input("What is your age?: ")

# inputed_age = checkDriverAge()

# if int(inputed_age) < 18:
# 	print("Sorry, you are too young to drive this car. Powering off")
# elif int(inputed_age) > 18:
# 	print("Powering On. Enjoy the ride!");
# elif int(inputed_age) == 18:
# 	print("Congratulations on your first year of driving. Enjoy the ride!")

#Doc strings are useful to provide some comments to your function with help of ''' your text ''' and when ever you call that function it will show as info while in ide (kind of f4 help )
# def test(a):
#   '''
#   this will print param a
#   '''
#   print(a)

# test(12)
# #help is a built in function to provide help for that function
# #help(test)
# #anaother way is using Magic method or dunder method in python __doc__ to prvide help
# print(test.__doc__)

#Excersice on OOPS
#Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def printname(self):
#         print(self.name, self.age)
#     def findoldcat(self):
#         if(int(self.age) >= 10):
#           print(f'{self.name} is old cat with age {self.age}')

# # 1 Instantiate the Cat object with 3 cats
# c1 = Cat('cat1','5')
# c2 = Cat('cat2','10')
# c3 = Cat('cat3','15')
# c1.printname()
# c2.printname()
# c3.printname()
# # 2 Create a function that finds the oldest cat
# c1.findoldcat()
# c2.findoldcat()
# c3.findoldcat()

# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# # did in above step

#Pure Functions
# def multiply_by2(li):
#   new_list = []
#   for item in li:
#     new_list.append(item*4)
#   return new_list

# print(multiply_by2([1,2,3]))

#Lambda functions / Lambda expressions
# here in replit its giving error - list object is not callable
#so tried in Jupyter notebook
# my_list = ['5','4','3']
# new_list = list([map(lambda num: num**2,my_list)])
# print(new_list)

#Modules in python
# import utility1
# import utility2
# print('Add numbers')
# print(utility1.add_num(2,30))
# print('Mul numbers')
# print(utility2.mul_num(2,30))

# #Importing module in another way to import specific functions/classes/methods from that module
# from utility1 import sub_num
# print('sub numbers')
# print(sub_num(20,10))

#we have built in modules like 'collections' that comes along with python3 download
from collections import Counter
import pdb

li = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8]

print(Counter(li))

pdb.set_trace()
str1 = 'jawahar reddy ch'
print(Counter(str1))

#Another Built in module datetime
import datetime

print(datetime.date.today())
print(datetime.date(2020, 3, 27))

#This systax will import function from other .pyfile

from Python_basics1 import function
