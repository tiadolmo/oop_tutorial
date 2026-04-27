# class definition
class employee:
    # object initialization
    def __init__(self, emp_id, emp_name, emp_depart, emp_post):
        self.eid = emp_id
        self.ename = emp_name
        self.edepart = emp_depart
        self.epost = emp_post
    
    # object methods
    def displayDetails(self):
        return f"""
            ID: {self.eid}
            Name: {self.ename}
            Department: {self.edepart}
            Position: {self.epost}
            """
        


# object instances
emp1 = employee(1,'Apple','IT','Maganer')
emp2 = employee(2, 'Banana', 'IT', 'Senior Developer')

# accessing attribute
print(emp1.ename)

# accessing methods
print(emp1.displayDetails())
