class Employee:

	#init is the constructor self is the object itself need not to pass
	def __init__(self, first , last, pay):
		self.first=first
		self.last=last
		self.pay=pay

	#method will also take self as parameter, because the object is
	#automatically passed as a parameter
	def fullname(self):
		return f"full name is {self.first} {self.last}"




emp_1 = Employee("suraj","mishra","50000")
print(emp_1.fullname())
# or can do it like
# the above gets coverted to below format this is why self is passed
print(Employee.fullname(emp_1))


# emp_2 = Employee("test","user","40000")

# print(emp_1.first)
# print(emp_2.first)