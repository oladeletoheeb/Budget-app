class Budget:
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    
    def deposit(self):
        return "this is a deposit"
    
    def withdraw_funds(self):
        return "withdraw funds"
    
    def check_balance(self):
        return "check your balance"
    
    def transfer(self):
        return " transfer balance"
    


category = Budget("Clothing", 2000)
category_1 = Budget("Food", 3000)
category_2 = Budget("Entertainment", 4000)

print(category.deposit())
print(category.withdraw_funds())
print(category.check_balance())
print(category.transfer())