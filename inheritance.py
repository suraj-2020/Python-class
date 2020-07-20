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

#inherits employee class
class Developer(Employee):
	raise_amount = 1.10
	def __init__(self, first , last, pay, prog_lang):
		super().__init__(first,last,pay)
		# can use Employee.__init__(self,first,last,pay)
		self.prog_lang=prog_lang

class Manager(Employee):
	
	def __init__(self, first , last, pay, employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees =[]
		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print("---->",emp.fullname())



dev_1 = Developer('Suraj','Mishra',50000,'python')
dev_2 = Developer('Niraj','Sharma',40000,'c++')
print(dev_1.pay)
print(dev_1.prog_lang)

mgr_1 = Manager('Sam','smith',90000,[dev_1])

mgr_1.print_emps()

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

#function provided by python
# EMployee will also be true but developer will be false(obvious)
print(isinstance(mgr_1, Manager))

#same provided by python
print(issubclass(Developer,Employee))