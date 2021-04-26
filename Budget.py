
class Category:


    def __init__(self, category,amount):
       self.category = category
       self.amount = amount

    def deposit(self, amount):
        self.amount += amount 
        return "You have successfully deposited  {} in {} category".format (amount, self.category)



    def budgetBalance(self):
        return "This is your current balance : {}".format(self.amount)

    
    def checkBalance(self, amount):
        if amount <= self.amount:
            return True 
        else :
            return False


    def Withdrawal(self, amount):
        self.amount -= amount 
        return "You have successfully withdrawn {} from {} category".format (amount, self.category)
        

    def Transfer(self, amount, category):
        if self.checkBalance(amount) is True:
            return self.Withdrawal(amount) + ' ' + category.deposit(amount)
        else:
            "You don't have enough funds in " + self.category + " to transfer"


foodCategory = Category ("food", 400)
clothingCategory = Category ("clothing", 500)  
vacationCategory = Category ("vacation", 600)
carCategory = Category ("car", 700)



print(foodCategory.deposit(200))
print(foodCategory.budgetBalance())
print(foodCategory.checkBalance(600))
print(vacationCategory.Withdrawal(300))
print(vacationCategory.budgetBalance())
print(carCategory.Transfer(400, vacationCategory))
