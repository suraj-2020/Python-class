class Employee:

	def __init__(self, first , last):
		self.first=first
		self.last=last 
	
	@property
	def fullname(self):
		return f"full name is {self.first} {self.last}"

	#this makes possible to use function as variables
	@property
	def email(self):
		return f"{self.first}.{self.last}@email.com"


	#setter can be used on methods that are having property decorator
	#i.e. @property is applied and it is made avaliable as variable
	@fullname.setter
	def fullname(self,name):
		first, last = name.split(' ')
		self.first=first
		self.last=last

	@fullname.deleter
	def fullname(self):
		print('Delete Name')
		self.first=None
		self.last=None


emp_1 = Employee('Suraj','Mishra')

emp_1.first = 'JIM'

print(emp_1.email)

emp_1.fullname="Niraj Mishra"

print(emp_1.first)

del emp_1.fullname