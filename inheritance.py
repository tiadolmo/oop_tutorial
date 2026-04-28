# parent class
class person:
    def __init__(self, name, age, gender):
        self.p_name = name
        self.p_age = age
        self.p_gender = gender

    def get_details(self):
        return f'''{self.p_name} is a {self.p_age} year old.'''
    

# child class 
class student(person):
    pass # it inherits all the properties and methods of the parent class without any modification

# # child instance
# s1 = student('Apple',10, 'male')
# print(s1.get_details())


# child class with modification
class teacher(person):
    def __init__(self, name, age, gender, subject): # it overrides the parent class constructor
        super().__init__(name, age, gender) # it calls the parent class constructor
        # person.__init__(name, age,  gender) # it calls the parent class constructor

        # adding new properties to the child class
        self.t_subject = subject

        # new method in the child class
    def teaches_subject(self):
            return f'{self.p_name} teaches {self.t_subject}.'
        
# child instance
t1 = teacher('Zebra',30, 'Female','Mathematics')
print(t1.teaches_subject())









# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         print("Hello from B")

# class C(A):
#     def greet(self):
#         print("Hello from C")

# class D(B, C):
#     pass

# obj = D()
# obj.greet()