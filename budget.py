class Budget:
    def __init__(self, category, amount):
		self.category = category
		self.amount = amount
		
	def deposit(self, amount):
		self.balance += amount
		
	def withdraw(self, amount):
		self.balance -= amount
		
	def transfer(self, amount, category):
		self.withdraw(amount)
		category.deposit(amount)
		
food = Budget('food', 2000)
clothing = Budget('clothing', 300)

food.withdraw(200)
clothing.deposit(500)

food.transfer(300, clothing)

print(food.balance)
print(clothing.balance)
