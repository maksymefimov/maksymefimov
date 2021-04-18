class Person:
    def __init__(self,name,age = 0):
        self.name = name
        self._age = age
    def display(self):
        print(self.name)
        print(self._age)
