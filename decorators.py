
#args and kwargs are added so it can take any number of argument
def decorator_function(original_function):
	#original_function is used as closure
	def wrapper_function(*args,**kwargs):
		print(f"Our wrapper executed this before {original_function.__name__}")
		return original_function(*args,**kwargs)
	return wrapper_function

#basically this will add functionality to the below function
@decorator_function
def display():
	print('display function ran')

@decorator_function
def display_info(name,age):
	print(f'display_info ran with arguments {name} {age}')

#that @decorator_function and this below are same
#upper one is more readable therefore more commonly used
#display = decorator_function(display)
display()

# display_infoa = decorator_function(display_info('JOhn',25))
# display_infoa
display_info('JOhn',25)

