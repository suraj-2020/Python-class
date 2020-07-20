#same as magic methods
class Employee:

	raise_amount = 1.04


	def __init__(self, first , last, pay):
		self.first=first
		self.last=last
		self.pay=pay 

	def fullname(self):
		return f"full name is {self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	#this returns something that is generally usable for developer
	#for ex the return type here can be directly used yo create object
	def  __repr__(self):
		return f"Employee('{self.first}','{self.last}','{self.pay}')"

	#if both presents returns str, this is more for user
	def __str__(self):
		return f"{self.fullname()}"

	def __add__(self, other):
		return self.pay+ other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Suraj','Mishra',50000)
emp_2 = Employee('Suraj','Mishra',40000)



print(emp_1)
print(repr(emp_1))#print(emp1.__repr__()) is same 

print(1+2) # this is equated to print(int.__add__(1,2))
print(len('Test'))# same as print('test'.__len__())

print(emp_1+emp_2)#overided add 