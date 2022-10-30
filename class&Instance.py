class Employee:
    Company="Tech Mahindra"                 # Class Variables
    pass

emp1=Employee()                             # Object Declartions
emp2=Employee()

emp1.name="Rohan"                           # Class Instance
emp2.name="Karan"

emp1.salary=15000
emp2.salary=17000

print(f"E_Name is : {emp1.name} E_Salary is : {emp1.salary} E_Company is : {Employee.Company}")

# Class Variable Can't Be Updated by using object instance. We have to use class variable to do so.
# Otherwise It will Another Entry in Object Dictionary.


