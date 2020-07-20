class Employee:

	#class variables 
	num_of_emps=0
	raise_amount = 1.04

	#constructor therefore runs every time a new employee object 
	# is created
	#The variables here are called instance variables
	def __init__(self, first , last, pay):
		self.first=first
		self.last=last
		self.pay=pay

		#here also self.num_of_emps could have been used
		# but it makes no sense as this needs to be update for
		# every object of that class
		Employee.num_of_emps +=1

	def fullname(self):
		return f"full name is {self.first} {self.last}"

	# can't directly use raise raise_amount as class variable
	# are not directly stored in object and can't directly be accesed
	# by methods so either use Employee.raise_amount or 
	# self.raise_amount. However if self.raise_amount is used 
	# it adds the class variable to object and now any changes
	# made is specific to that object only
	

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("suraj","mishra",50000)
emp_2 = Employee("test","user",40000)
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)
print(Employee.num_of_emps)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)