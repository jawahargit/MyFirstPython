def function():
  print("Hi Jawahar Reddy")
  #Operator Precedense
  #Means Priirty order that operater executes in python

  # () brackets
  # **  and // --Power of and floor division
  # * and /    -----Multiplication and  division
  # + and -    -----Addition and  substraction

#   print((2*3)+(3+4)-(4*4))
#   # 6+7-16
#   # 13-16
#   # ans = -3

#   print((2*3)-(3+4)+(4*4))
#   # 6-7+16
#   # -1+16
#   # ans = 15

#   #Augumented assignment operator / Short hand notation
#   # +=
#   # -+
# print("Augumented operator += or -= or *= ")

#string operations 
# mystr = 'to be or not to be'
# print(mystr.replace('be', 'me'))
# #String slicing [stat:end:stepsize]
# b = "Hello, World!"
# print(b[2:5:2])
# print(b[::-1]) # string reverse

# Login page
# name = input('your name:')
# age = input('age:')
# birth_year = input('Your birth year:')
# new_age = 2022 - int(birth_year)
# print(f'your new age is {new_age}')
# print('your name ',name)
# print('your age ' ,age)
# print('your birth year',birth_year)


  
#Data Structures - which are like store the data
# List and Dictionary , Sets  and Tuple are 4 type of built in datdata structurres in python
#List is ordered pair key data strucutre that stored in memeory
#Dictionary is unordered pair 
#List is like a book shelf ordered one after the other in the memeory .
#Dictionary is like storing the data randaomly in memeory and with key we retreve the values

  

# #Lists
# #List slicing
# print('list slicing')
# li = [1,2,3,4]
# li2 = ['a','b','c']

# print(li[0:2])
# print(li2[::-1])

# li = li2[:]

# li[0]= 'X'
# print(li)
# print(li2)


# #List methods
# print('list methods')
# list1 = ['a','b','c','d','e','f','x','z']
# list1.append(5) # append 5 to last of the list
# print(list1)
# pop_1 = list1.pop(5) # here 5 indicates index
# print(pop_1)  #output = f
# list1.reverse() # reversing the list with reverse method and reverse method return none
# print(list1) 
# print(list1[::-1]) #list slicing method for reverse order this will do same as reverse method did 

# #to generate a numbered list 
# print(list(range(1,100))) # produce a list from 1 to 99

# #Join method , we use often join method to join strings which are in lists
# sentense = ','
# new_sentense = sentense.join( ['hi','jawahar','welcome','to','AI'] )
# print(new_sentense) # hi,jawahar,welcome,to,AI

# #list unpacking
# print('list unpacking')
# a,b,c,*other,z = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(a) #1
# print(b) #2
# print(c) #3
# print(other)  # [4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(z) #12


# #Matrix
# #here list is nothing but arrays in a matrix 
# #Matrix is group of lists or arrays 
# print('Matrix operations')
# matrix = [
#   [1,2,3],
#   [5,6,7],
#   [9,1,3]
# ]
# print(matrix)
# #change list values in a matrix 
# matrix[0] = [1,1,1]
# print(matrix)
# #chnage a particular list value inside a list in a matrix
# matrix[1][0] = 9
# print(matrix)
# #Matrix reversal
# print(matrix[::-1])
# #function()


# #Dictionary
# #Dictoanry systax is same like JSON format
# #2 ways we can write dictionaries
# print("Dictonary")
# dic1 = {
#   'a' : [1,2,3],
#   'b' : ['jaw',23,24,'reddy'],
#   'c' : ['kalyani','lohansh']
# }

# #dictionary inside a list 
# dic2 = [
# {
#   'a' : [4,5,6],
#   'b' : ['jaw',27,28,'reddy'],
#   'c' : ['kalyani','lohansh']
# },
#   {
#   'a' : [1,2,3,7],
#   'b' : ['jaw',23,24,'reddy'],
#   'c' : ['kalyani','lohansh']
# },
#   {
#   'a' : [1,2,3,9],
#   'b' : ['jaw',23,24,'reddy'],
#   'c' : ['kalyani','lohansh']
# }
# ]


# print(dic1['a'][1])  #2
# print(dic2[1]['b'][0]) #jaw


#COndtinal if ststaements 

# is_magician = True
# is_expert = True

# if is_magician and is_expert :
#   print("You are master magician")
# elif is_magician and not is_expert :
#   print("You are magician and not expert")
# elif not is_magician:
#   print("You are not magician")
# print(True == 1)
# a = 'xyz'
# b = 'xyz'
# print(a is b)