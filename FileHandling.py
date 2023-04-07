'''What is File function in python? What is keywords to create and write
file.'''

'''File function is used to create,read,and write file using python. Keyword create is used for creating 
   empty file and write is used for writing to file'''

'''Write a Python program to read an entire text file
'''
#open and read file
f=open("myfile.txt","r")
print(f.read())


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

class Rectangle:
   
    #create constructor
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    #create a method for calculating area
    def calculateRectangle(self):
        print(self.length*self.width)
    


obj=Rectangle()
obj.calculateRectangle()
print(obj)












