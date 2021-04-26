 #loop

       #FOR LOOP
#fruits = ["apple","banana","cherry"]
#for x in fruits: 
  #print(x)

#for x in "banana": 
  #print(x)

  #fruits = ["apple","banana","cherry"]
  #print(x)
      #if x == "banana":
          #break
#fruits = ["apple","banana","cherry"]
#for x in fruits:
    #if x == "banana":
        #break
    #print(x)
  
       #WHILE LOOP
#i = 1
#while i < 6:
    #print(i)
    #i+=1

 
             #Functions 


 #define,print, call the function 
#def my_function():
  #print("Hello from a function")
#my_function()


#DefaultValue
#def my_function(country = "Ghana"):
 #print(" I am from " + country)
#my_function()

#arguments(specicfied after the function name)
#def my_function(fname):
  #print(fname + "Refsnes")
#my_function("kelvin")
#my_function("alvin")
#my_function("claire") 

#ReturnValue (basically calling for an action)
#def my_function(x):
  #return 5 * x
#print(my_function(77))


#Pass Statement
#def myfunction():
   #pass


   #passing a list as  an argument 

#def my_function(food):
  #for x in food:
    #print (x)

#fruits = ["apple","banana","cherry"]

#my_function(fruits)


             #Dictionary ( store data in key value pairs)

#thisdict = {"brand":"Ford","model":"Mustang","year":1964}
#print(thisdict)

      #dictionary Items

#thisdict = {"brand":"Ford","model":"Mustang","year":1964}
#print(thisdict["brand"])
 

 #Ordered = follow a pattern version 3.7
 #Unordered = no defined order or patteren version 3.6

 #Changeable = add, remove once  the dictionary has been created 

 #Duplicates are not allowed .

#thisdict = {"brand":"Ford","model":"Mustang","year":1964,"year":2020}
#print(thisdict)


  #Try .... Except , Finally 

#try:
    #print(x)
#except:
    #print("An exception occured")

   #Many exceptions

#try:
 # print("y")
#except NameError:
  #print("Varriable  y is not defined")
#except :
  #print("something went wronng")


#try:
 # print("Hello World")
#except:
 # print("Something went wrong")
#else:
 # print("Nothhing went wrong")

#try:
 #print(x)
#except:
 #print("Something went wrong")
#finally:
 #print("The 'try except' is finished")


    #This can be useful to close objects and clean up resources:


#f = open("demofile.txt")
  #f.write("Lorum Ipsum")
#except:
  #print("Something went wrong when writing to the file")
#finally:
  #f.close()

                                 #OOP

##class Car :
  
  #def _init_ (self, name, color):
      
      #self.model = name
      #self.color = color 

  #def my_Car(self):
    #print("My car's model is", self.model) 

  #myCar1 = Car ("BMW", "White")
  #myCar1.model = "Toyota" 
  #myCar1.my_Car() 



# def __init__(self, fname, lname):
 
    #self.firstname =fname
    #self.lastname =lname

  #def printname(self):
   
  #print(self.firstname,self.lastname)


#x = Person("Kelvin" ,"Tagoe")

#x.printname()







#class Person :
  
  #def __init__(self, fname, lname):
    #self.firstname =fname
    #self.lastname =lname

  #def printname(self):
   
  #print(self.firstname,self.lastname)

# create a child  

#class Student(Person):
  
  pass 


#x = Person("Kelvin" ,"Tagoe")

#x.printname()




# the super() function makes the child inherit everything from the paerent.
# the _init_() function when used makes the child no longer inherit the parent, it causes an override
# properties can be added to the child same way properties was added to the parents 
# methods can be defined in the child class just like the parent class 
#Refer to slides 

                                #Super Function                   
#class Person:

  #def __init__(self, fname, lname):

    #self.firstname = fname

    #self.lastname = lname

 

  #def printname(self):

  #print(self.firstname, self.lastname)

 

#class Student(Person):

  #def __init__(self, fname, lname):

  #super().__init__(fname, lname)

 

#myStudent = Student("Mike", "Olsen")

#myStudent.printname()






                           #methods

#def __init__(self, fname, lname):

  
  #self.firstname =fname
  #self.lasttname =lname
 

  #def printname(self):

  #class Student(Person):

  #def __init__(self, fname, lname,age,gender):

    #super().__init__(fname, lname)

    #self.age = age

    #self.gender = gender

 

#myStudent = Student("Mike", "Olsen", 29,"male" )

#print(myStudent.age, ",",myStudent.gender)







            #methods 
#class Person:

  #def __init__(self, fname, lname):

    #self.firstname = fname

    #self.lastname = lname

 

  #def printname(self):

    #print(self.firstname, self.lastname)

 

#class Student(Person):

  #def __init__(self, fname, lname,age, gender):

    #super().__init__(fname, lname)

    #self.age = age

    #self.gender = gender

  #def student_profile(self):

    #print("The student profile is listed below")

    #print("Firstname- ", self.firstname)

    #print("Lastname - ", self.lastname)

    #print("Age - ", self.age)

    #print("Gender - ", self.gender)

 

 

#x = Student("Mike", "Olsen",24,"male")

#x.student_profile()


