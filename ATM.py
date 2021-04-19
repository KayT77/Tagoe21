import  datetime
now = datetime.datetime.now()
print('Welcome to TAG ATM,Current date and time is:')
print(now.strftime("%y-%m-%d %H:%M:%S"))

name = input("Please enter  your name? \n")
allowedUsers = ["Alvin","Kelvin","Claire"]
allowedPasswords = ["alpha","beta","gama"]
Balance = [200,300,400]
selectedOption = 1

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    if (password == allowedPasswords[userId]):
        print('Welcome ' + name)
        print('Please select your transaction:')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Complaint')
        selectedOption = int(input('Please select your transaction:'))

        if(selectedOption == 1):
            print('You selected %s' % selectedOption + ': Withdrawal')
            withdrawalAmount = input('How much would you like to withdraw?')
            print('Take your cash.')
                 
           
        elif(selectedOption == 2):
            print('You selected %s' % selectedOption + ':Deposit')
            depositAmount = int(input('How much would you like to deposit?'))
            userBalance    = allowedUsers.index(name)
            currentBalance = (Balance[userId])
            newBalance = str(currentBalance + depositAmount)
            print('Your New Balance is $' + newBalance)
                   
                
        elif(selectedOption == 3):
            print('You selected %s' % selectedOption + ':Complaint')
            complaint = input('What issue would you like to report?')
            print('Thank you for contacting us.')

        else:
            print('Invalid transaction,please try again')

    else:
        print('Password incorrect,please try again')

else:
    print('Username incprrect,please try again')


         
                 
    