class emp:

    def __init__(self,name,sal):
        self.name=name
        self.salary=sal
    
    def give_name(self):
        return f"The name of the employee is {self.name}"

    def give_sal(self):
        return f"The salary of the {self.name} is {self.salary}"

e1= emp("suraj",500)
#print(e1)
print(e1.give_sal())
