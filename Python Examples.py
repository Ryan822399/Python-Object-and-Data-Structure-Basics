# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:41:09 2020

@author: Ryan's Computer
Python Object and Data Structure Basics
"""

#Section 11: arithmetic operations
print(2+2)
print(2*3)
print(1/2)
print(2**3)


#Section 13: Variable Assignments
#python variables are dynamic versus static
#use type() function to check things like int, string, bool, float
a = 5
print(a)
a = 10
print(a)
print(a+a)
a=(a+a)
print(a)
print(type(a))
a = 30.1
print(a)
print(type(a))


#Section 14: Strings
#can use either '' or ""
a= 'hello'
a = "hello"
print(len(a))


#Section 15: Indexing and slicing
print(a[1])     #strings can be indexed similar to arrays
print(a[-1])    #they can also be index backwards using negative indexes
print(a[:3])
print(a[2:])
print(a[2:4])   
print(a[0:5:2]) #traverses through the string skipping every other character  
print(a[::-1])  #reverses the string


#Section 16: String Properties
x = "Hello World"
x = x + " it is cool outside"   #string concatination
print(x)
x = x*2                         #prints out tow of the string
print(x)
x = "hello world"
print(x.upper())
print(x.split())
x = "Hi this is a string"
print(x.split("i"))


#Section 18 Print Formatting
print("This is a string {}".format("INSERTED"))
print("the {2} {1} {0}".format("fox", "brown", "quick"))        #parameter indexing using numbers 
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))  #paramter indexing using keywords
result = 100/777                                        
print("the result was {r:1.3f}".format(r=result))               #float formatting for sig figs (this one is 3 decimal places)
name = "Jose"
print(f"Hello, his name is {name}")                             #String formatting using f strings


#Section 20: Lists
myList = [1,2,3]
myList = ['String', 123, 1]    #lists can mix data types
#they follow similar rules to strings as far as indexing and splicing
myList.append(1)
print(myList)
print(myList.pop())
alphabetList = ['a', 'e', 'h', 'b']
numList = [1, 9, 3, 5, 2, 7, 42]
alphabetList.sort()             #easy built in sorting methods
numList.sort()
print(alphabetList)
print(numList)
numList.reverse()
print(numList)                  #reverse an array


#Section 22: Dictionaries
myDict = {'key1':'value1', 'key2':'value2'}
print(myDict['key1']) 
d = {'k1':123, 'k2':[0,1,2], 'k3':{'dict2':'result3'}}  #dctionaries support lists and dictionaries inside of them
print(d['k3']['dict2'])
d['k1'] = "NEW"                                         #re assign a key
print(d['k1'])
print(d.keys())
print(d.values())
print(d.items())

#Section 24: Tuples
t = (1, 2, 3, "Hello")
print(t)
print(t[1])
t = ('a', 'a', 'b')
print(t.count('a'))                                     #returns the amount of the passed in item
print(t.index('a'))
#t[0] = 2                                               #tuples cannot be mutated


#Section 25: Sets
myset = set()
myset.add(1)
print(myset)
myset.add(2)
myset.add(2)
print(myset)                                            #sets can only contain unique values
mylist = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5]
print(set(mylist))                                      #casting a set

#Section 26: Booleans
print(type(False))                                      #bools must be capitalized
print(1 > 2)
print(1 == 2)
b = None                                                #Use None for setting a datatype to nothing

#Section 27 I/O with Basic Files
myfile = open('myfile.txt')
print(myfile.read())
print("nothing" + myfile.read())
myfile.seek(0)
print("after seeking" + myfile.read())
myfile.seek(0)
print(myfile.readlines())

with open('myfile.txt', mode='r') as my_new_file:                 #NOTE: this is best practice for opening files
    contentes = my_new_file.read()                                #files have multiple different modes
with open('myfile.txt', mode='a') as f:                 
    f.write('\nHELLO')
with open('myfile.txt', mode='r') as f:                 
    print(f.read())
    




