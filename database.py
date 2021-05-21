# Create ,Read, Update,Delete
#CRUD

#find user


import os
import validation

user_db_path = "data/user_record/"
user_auth_session_path = "data/auth_session/"

def create(accountNumber, firstName, lastName, email, password):
   
    userData = firstName + "," + lastName + "," + email + "," + password + "," + str(0)


    if doesAccountNumberExist(accountNumber):

       return False

    if doesEmailExist(email):
        print("User already exists")
        return False

    completionState =False 

    try:

        f = open(user_db_path + str(accountNumber) + ".txt", "x")

    except FileExistsError:
        
        doesFileContainData = read(user_db_path + str(accountNumber) + ".txt")
        if not doesFileContainData:
            delete(accountNumber)

    else:

        f.write(str(userData))
        completionState = True 

    finally :

        f.close()
        completionState



def read(accountNumber):

   
    isValidAccountNumber = validation.accountNumberValidation(accountNumber)

    try:

        if isValidAccountNumber:
            f = open(user_db_path + str(accountNumber) + ".txt", "r")
        else:
            f = open(user_db_path + accountNumber, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False






def update(accountNumber, user_details):

    user = user_details[0] + "," + user_details[1] + "," + user_details[2] + "," + user_details[3] + "," + user_details[4]
    
    try:
        f = open(user_db_path + str(accountNumber) + ".txt", "w")
        f.write(user)
        return True
    except:
        return False




def delete(accountNumber):

    isDeleteSuccessful = False

    if os.path.exists(user_db_path + str(accountNumber) + ".txt"):

        try:

            os.remove(user_db_path + str(accountNumber) + ".txt")
            isDeleteSuccessful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return isDeleteSuccessful




def doesEmailExist(email):

    allUsers = os.listdir(user_db_path)

    for user in allUsers:
        
        userList = str.split(read(user), ',')
        
        if email in userList:
            return True
    return False



def doesAccountNumberExist(accountNumber):

    allUsers = os.listdir(user_db_path)

    for user in allUsers:

        if user == str(accountNumber) + ".txt":

            return True

    return False




def authenticatedUser(accountNumber, password):

    if doesAccountNumberExist(accountNumber):

        user = str.split(read(accountNumber), ',')

        if password == user[3]:
            return user


    return False


def login_auth_session(accountNumber, userDetails):
     
    data = userDetails [0] + "  " + userDetails [1] + " test log in"

    try:

        f = open(user_auth_session_path + str(accountNumber) + ".text", "x")

    except FileExistsError:

        f = open(user_auth_session_path + str(accountNumber) + ".text", "w")  
         
    else:
        f.write(data)

    finally:
        f.close()

    return True


def logout_auth_session(accountNumber ,userDetails):

    if os.path.exists(user_auth_session_path + str (accountNumber) + ".text"):
       os.remove(user_auth_session_path + str(accountNumber) +".text") 

    else:
        print("File does not exist")














 