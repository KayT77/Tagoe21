#Create File (database.py)
#Record
#Update
#Read

import os 
import validation

user_db_path = "data/user_record/"


def create (userAccountNumber,first_name, last_name, email, password):
    #create file 
    #name of file accountNumber.txt
    #add details to file 
    #return true 

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(userAccountNumber):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(userAccountNumber) + ".txt", "x")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(userAccountNumber) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)

    else:

        f.write(str(user_data)):
        completion_state = True

    finally:

        f.close():
        return completion_state


def update (userAccountNumber):
    #find user with account number 
    #fetch content of file 
    #improve content of file 
    #save file 
    #return true

    isValidAccountNumber = validation.accountNumberValidation(userAccountNumber)

    try:

        if isValidAccountNumber:
            f = open(user_db_path + str(userAccountNumber) + ".txt", "r")
        else:
            f = open(user_db_path + userAccountNumber, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def read (userAccountNumber)
    #find user with account number 
    #fetch content of the file 

def delete (userAccountNumber):
    #find user with account number 
    #delete user record / file 
    #return true 
    
    is_delete_successful = False

    if os.path.exists(user_db_path + str(userAccountNumber) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful



 def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(accountNumber):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(accountNumber) + ".txt":

            return True

    return False


def authenticatedUser(accountNumber, password):

    if doesAccountNumberExist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False

