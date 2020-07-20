#same applies in js
#basically first class functions are those functions which are
#returned as variables can be passed on as variables without 
#getting executued. therefore no () is usedd while using 
#first class function. Nothing needs to be done explicitly
#this is functionality of python and JS which is having a name
#of first class function should now that this is possible and
#is used
def square(x):
	return x*x

def cube(x):
	return x*x*x

def my_map(func, arg_list):
	result=[]
	for i in arg_list:
		result.append(func(i))
	return result

squares = my_map(square, [1,2,3,4,5])
cubes = my_map(cube, [1,2,3,4,5])

print(squares)
print(cubes)