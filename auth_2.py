import random
import validation
import  database
import  datetime
now = datetime.datetime.now()

accountNumberFromUser = None

def init ():

    print('Welcome to TAG Bank')
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    haveAccount = int (input("Do You have an account with us: 1 (Yes) 2 (No) \n"))

    if (haveAccount==1):
           
        login()

    elif(haveAccount==2):
           
        register()
    else:
        print("You have selceted an invalid option") 
        init()


def login():

    print("*******Login*******")

    global accountNumberFromUser
    accountNumberFromUser = input("What is Your Account Number?\n")
    
    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)
    
    if isValidAccountNumber:

        password = input("What is your password?\n")

        user = database.authenticatedUser(accountNumberFromUser, password);

        if user:
            database.login_auth_session(accountNumberFromUser, user)
            bankOperation(user)  
        
            print('Invalid account or password')
            login()
        
    else:
        print("Account Number Invalid: check if account is up to 10 digits and only intergers")
        init()
        

    
def register():
    
    print("Register Your Account")
   
    email = input("What is  your email address?\n")
    firstName = input("What is your First Name?\n")
    lastName =  input("What is your Last Name?\n")
    password = input("Create password \n")
 
    accountNumber = generationAccountNumber()

    isUserCreated = database.create(accountNumber,firstName, lastName, email, password)
    
    if isUserCreated:

        print("Your Account has been Created")
        print(" == === ====== ===")
        print("Your account number is: %d" % accountNumber)
        print("Please Keep  Your Account Number safe")
        print(" == === ====== ===== ===")
    
        login()

    else:
        print("Something went wrong, Please try again")
        register()


             
def bankOperation(user):

    print("welcome %s %s " % (user[0],  user[1]))
    
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) logout (4) Exit \n"))
    
    if(selectedOption == 1):

        depositOperation(user)
    elif(selectedOption == 2):

        withdrawalOperation(user)
    elif(selectedOption == 3):

        logout()  
    elif(selectedOption == 4):

        exit()
    else:

        print("Invalid Transaction selected")
        bankOperation(user)



def withdrawalOperation(user):
    currentBalance = int(getCurrentBalance(user))
    amountToWithdraw = int(input("How much do you want to Withdraw?"))
    currentBalance -= amountToWithdraw
    setCurrentBalance(user, str(currentBalance))


    if database.update(accountNumberFromUser,):
        print("Your account balance is {}".format(currentBalance))
        bankOperation(user)
    
    else:
        print("Unsuccessful Transaction")
        bankOperation(user)
    


def depositOperation (user ):
    currentBalance = int(getCurrentBalance(user))
    amountToDeposit = int(input("How much do you want to deposit?"))
    currentBalance += amountToDeposit
    setCurrentBalance(user, str(currentBalance))

    if database.update(accountNumberFromUser, user):
        print("Your account balance is {}".format(currentBalance))
        bankOperation(user)
    
    else:
        print("Unsuccessful Transaction")
        bankOperation(user)




def generationAccountNumber():
    return random.randrange(1111111111,9999999999)


def setCurrentBalance(userDetails, balance):
    userDetails[4] = balance


def getCurrentBalance(userDetails):
    return userDetails[4]


def logout():
    login()


init()
#print(generateAccountNumber())

