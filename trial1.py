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

