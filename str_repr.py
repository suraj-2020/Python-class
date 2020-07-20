a =[1,2,3,4]
b = 'sample string'

#the goal of str is to be readable
#goal of repr is to be unambigious for ex when using datetime
#str will return date and time in readable format
#but repr will return the object here datetime
print(str(a))
print(repr(a))

print(str(b))
print(repr(b))