#same is in JS
def outer_func():
	message = "HI"

	#message in inner_function is called "free variable"
	#because it is not defined in this function but it still
	#has access to it because it is insided outer_func
	def inner_func():
		print(message)

	#returning function this way , in this case it will be executed
	return inner_func()

outer_func()

#A closure is an inner function that remembers and has access to variables
#in the local scope in which it was created even after the outer
#function has finish executing
def outer_func2(msg):
	message = msg

	#message in inner_function is called "free variable"
	#because it is not defined in this function but it still
	#has access to it because it is insided outer_func
	#CAN DIRECTLY PRINT msg WILL WORK THE SAME
	def inner_func2():
		print(message)

	#returning function this way , in this case it will be executed
	return inner_func2

hi_func=outer_func2("hi from 2") #now here hi_func is equal to inner_func2
hello_func=outer_func2("hello from 2")
#therefore a closure closes over the free variables from their 
#enviroment
#notice how we need not send any data to hi_func anad hello_func
#both are empty paranthesis, they both were returned as variables
# by which they remebered the variables in their parent function
#even after it was finished executing (a propert of first class functions , this is closure)
hi_func()
hello_func()