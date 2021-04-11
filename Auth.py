
import random
import  datetime
now = datetime.datetime.now()

#name = input("Please enter  your name? \n")
#allowedUsers = ["Alvin","Kelvin","Claire"]
#allowedPasswords = ["alpha","beta","gama"]

allowedUserDictionary = {
    'Alvin' :'alpha',
    'Kelvin' : 'beta',
    'Claire' : 'gama'
}

database_user = {
    'Alvin': 'alpha',
    'Kelvin' : 'beta',
    'Claire' : 'gama'
}


database = {}  #dictionary

def init ():

    print('Welcome to TAG Bank')
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    haveAccount = int (input("Do You have an account with us: 1 (Yes) 2 (No) \n"))

    if (haveAccount==1):
           
             login ()
    elif(haveAccount==2):
           
              print(register())
    else:
           print("You have selceted an invalid option") 
           init()

def login():
    
    print("*******Login*******")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input ("What is Your Password? \n")

    for accountNumber,userDetails in database.items():
        if (accountNumber == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOperations(userDetails)  
                

    print('Invalid Account or Password')
    login()
    
    

def register():
    
    print("Register Your Account")
   
    email = input("What is  your email address?\n")
    first_name = input("What is your First Name?\n")
    last_name =  input("What is your Last Name?\n")
    password = input("Create password \n")
 
    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account has been Created")
    print(" == === ====== ===")
    print("Your account number is: %d" %accountNumber)
    print("Please Keep  Your Account Number safe")
    print(" == === ====== ===== ===")
    login()

def bankOperations(user):

    
    print("welcome %s %s " % (user [0],user[1]))
    
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Complaint')
    print('4. Logout')
    selectedOption = int(input("Please select your Transaction :"))
    
    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation()
    elif(selectedOption == 3):

        logout  
    elif(selectedOption == 4):

        exit()
    else:

        print("Invalid Transaction selected")
        bankOperations(user)

def withdrawalOperation():
    print("How much would you like to withdraw? \n") 
    print("Take Cash")


def depositOperation ():
    print("How much would you like to Deposit? \n")
    print("Cash received")

def complaintOperation ():
    print("What issue would you like to report today?")
    print("Thank you for contacting us")


def logout():
    login()




def generationAccountNumber():
    
    return random.randrange(1111111111,9999999999)



init()
#print(generateAccountNumber())

 
 