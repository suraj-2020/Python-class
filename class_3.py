class Employee:

	num_of_emps=0
	raise_amount = 1.04


	def __init__(self, first , last, pay):
		self.first=first
		self.last=last
		self.pay=pay
		Employee.num_of_emps +=1

	def fullname(self):
		return f"full name is {self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first,last,pay)

	#static methods are methods inside a class that usually
	#do not use any variabele of class and not take object or class
	#as a parameter. It's like a normal function inside a class.
	@staticmethod
	def is_workday(day):
		if day.weekday() ==5 or day.weekday() ==6:
			return False
		return True

emp_1 = Employee("suraj","mishra",50000)
emp_2 = Employee("test","user",40000)

#this will output 1.04(default set in class)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#class method therefore will take class as an argument(cls)
Employee.set_raise_amt(1.05)

# this could also be used by instance
# emp_1.set_raise_amt(1.04) 

# this will yeild the same result but dosen't make sense 
# as while using object's method it should ideally change 
# only it's properties

# as class was taken as an argument all it's instances(objects) have there
# raise_amount updated to 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 ='john-doe-70000'
emp_str_2 ='jabne-doe-80000'
emp_str_3 ='steve-doe-30000'

#using class method as alternative to constructor
#if there is a use case where a string is passed and after preprocessing it
#we get attribute of that object, then doing that in class method
#assiging variables value and then returning it can be used
#to create an object with initialized values
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.first)

import datetime

my_date = datetime.date(2020,7,7)

print(Employee.is_workday(my_date))

