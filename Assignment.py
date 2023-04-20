'''What is File function in python? What is keywords to create and write
file.'''

'''File function is used to create,read,and write file using python. Keyword create is used for creating 
   empty file and write is used for writing to file'''

'''Write a Python program to read an entire text file
'''
#open and read file
f=open("myfile.txt","r")
print(f.read())
f.close()

#Write a Python program to append text to a file and display the text. 
#open and append to file
f= open("myfile.txt","a")    
f.write("Python")
f.close()

'''Write a Python program to read first n lines of a file. 

'''

#open and read the file
f = open("myfile.txt", "r")
#using readline() to get the entire line.

print(f.readline())
f.close()

# #Write a Python program to read a file line by line and store it into a list

with open('myfile.txt') as myfile3:
    text = myfile3.readlines()
# use strip to remove whitespace characters like `\n` at the end of each line
    for x in text:
        li=x.strip() 
        print(li)
myfile3.close()
# #Write a python program to find the longest words. 
#open the file and read
f5=open("myfile.txt","r")
print(f5.readline())
#create a function to find longest word
def findlongword(word):
    wordlist=[]
    maxlength=0
    for words in word:
        #loop through each word in file 
        #condition statement
        #check if length of words > maxlength if so set maxlength to words length
        if len(words)>maxlength:
            maxlength=len(words)
            #if length is equal to max length then add the words to the empty list and return it at the end.
        elif len(words)==maxlength:
            wordlist.append(words)
    return wordlist
w=findlongword(f5)
print("The longest word is:",w)

 #Write a Python program to copy the contents of a file to another file
 #first part of the code is to read the myfile and store the code to the second file(file2)
with open("myfile.txt",mode='r') as myfile,open('myfile2.txt','a') as myfile2:
    #running loop and individually storing each text to file 2
    for text in myfile:
        myfile2.write(text)


'''
Explain Exception handling? What is an Error in Python?
Exception handling is a way to respond to unexpected events using
try and except in python. There are two errors type:logical and syntax errors
'''

'''
How many except statements can a try-except block have? 
Name Some built-in exception classes:
 At least one except statements. Here are few built-in exceptions:valueerror,
 keyerror,Indexerror,ZeroDivisionError,etc.
'''
'''
When will the else part of try-except-else be executed?
The else part of try-except-else is executed when no exception happens.
'''
'''Can one block of except statements handle multiple exception?
 Yes. one block of except statements can handle multiple exceptions.
 
'''

# '''When is the finally block executed?
# Finally block is always executed after try/except.
# '''

# '''How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets'''
# #try block
try:
    a=1
    b="f"
    mul=1*b
 #except if it is different output than try
except:
    print("Invalid input")

else:
    print("Welcome")

#finally will always occur regardless of the output. 
finally:
    print("Thank you for using the application")


# '''What happens when "1"== 1 is executed?
# It gives a false.
# '''
# '''Write python program that user to enter only odd numbers, 
# else will raise an exception.'''

# #user defined exception
class EvenException(Exception):
 pass

try:
    #accept odd numbers from user
    num1= int(input("Enter only odd numbers:"))
    #check condition
    if num1%2!=0:
        print("Odd Number")
    else:
     #raise exception
     raise EvenException
    
    
except EvenException:
    print("User input is even number")
    
# #Tasks
# '''
# Accept a number from a user raise exception if user enter below zero value
# '''
# #user defined Exception
class belowZero(Exception):
   pass

#user input
num= int(input("Enter a number:"))

try:
   #check condition
   if num>0:
      print("postive")
   else:
   #raise exception
    raise belowZero

except belowZero:
   print("Your number is below zero")


#compare two numbers and raise a exception if first number is smaller than second number

#user defined Exception
class compare_Number(Exception):
   pass
#user input
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number:"))

try:
   #check condition
   if num1<num2:
      print("num2 is greater")
   else:
      #raise exception
      raise compare_Number
except compare_Number:
   print("Num1 is smaller than num2")
   

# '''What are oops concepts? Is multiple inheritance supported in python?'''

# '''There are four pillars of oops.Abstraction,polymorphism,inheritance,and encapsulation. Multiple inheritance is supported in python.'''

# '''How to Define a Class in Python? What Is Self? Give An Example Of
# A Python Class '''
# ''' 
# Class is a collection of data types which contains data members and member functions. Self which represents current class properties.


# '''

class Student:
    #data members
    name="Sam"
    subject="Intro to c++ programming"
    department="Computer Science"
    #member functions
    def display(self):
        print("Name: ",self.name,"Subject: ",self.subject,"department: ",self.department)
        
    #create an object
obj=Student()
#print obj
print(obj.display())


# '''Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle'''

#create a class

class Rectangle:
    #create a constructor
    def __init__(self,length,width): 
        self.length=length
        self.width=width
    #function to calculate rectangle area
    def calculateArea(self):
        print("Total Area:",self.length*self.width)
    
   #create a object of rectangle class and pass the argument 
obj=Rectangle(10,20)
#call calculate method
obj.calculateArea()
print(obj)

'''Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle'''

class Circle:
    #constructor
    
    def __init__(self,radius):
        self.rad=radius
    #member function
    def area(self):
        print(self.rad*self.rad*3.14)
    
    def perimeter(self):
        print(self.rad*2*3.14)
#create object
obj= Circle(4)
obj.area()
obj.perimeter()


'''Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python? '''

'''When one class derive from another class. Using inheritance helps reduce and reuse the code.'''
'''Example:'''

#parent class or base class
class Parent:
     def home(self):
         print("House in Rajkot")

#child class derives properties from base class
class child(Parent):
    def car(self):
        print("I have a car")
        
#create child object
obj=child()
obj.car()
obj.home()

'''init is a default constructor to initalize the object state.'''


'''What is Instantiation in terms of OOP terminology?

Instantiation: The creation of an instance of a class.

'''
'''What is used to check whether an object o is an instance of class A? '''
'''
isinstance() function
'''
