
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
        pass


    def Withdrawal(self, amount):
        self.amount -= amount 
        return "You have successfully withdrawn {} from {} category".format (amount, self.category)


    def Transfer(self, amount, category):
        pass


foodCategory = Category ("food", 400)
clothingCategory = Category ("clothing", 500)  
vacationCategory = Category ("vacation", 600)
carCategory = Category ("car", 700)



print(foodCategory.deposit(200))
print(foodCategory.budgetBalance())
print(vacationCategory.Withdrawal(300))
print(vacationCategory.budgetBalance())
