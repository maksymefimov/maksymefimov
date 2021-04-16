##1. В класі Person визначте метод compare_age(),
##який повертатиме результат порівняння віку людини з Вашим віком.
##При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
##буде повертатися повідомлення наступного формату:
##{other_person} is {older than / younger than / the same age as} me.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_age(self):
        my_age = 31
        if self.age > my_age:
            return self.name + ' is older than me!'
        elif self.age < my_age:
            return self.name + ' is younger than me!'    
        else:
            return self.name + ' is the same age as me!'   
            
        
