##2. Визначте атрибути fullname та email в класі Employee.
##При заданих first та last names:- В конструкторі сформуйте fullname
##звичайним з’єднанням через пробіл first та last name.
##В конструкторі сформуйте email з’єднанням first та last name через
##‘.’ між ними та приєднуючи  ‘@company.com’ наприкінці.
class Employee:
    def __init__(self, first,last_name):
        self.first = first
        self.last_name = last_name
        self.fullname = first + ' ' + last_name
        self.email = first + '.' + last_name + '@company.com'
        
    
