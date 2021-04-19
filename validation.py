def accountNumberValidation(accountNumber):

    if accountNumber :

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError :
                print("Invalid account number")
                return False 
            except TypeError :
                print("Invalid account type")
                return False 
        
        else:
            print("Account number cannnot be less or more  than 10 digits")

    else:
        print("Account number is required") 