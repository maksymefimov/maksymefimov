##3. В класі Name визначте:
##атрибути для first name та last name (fname та lname відповідно);
##атрибут fullname що повертає first і last names;
##атрибут initials який повертає ініціали
##(перші літери first та last name, розділених ‘.’ .
class Name:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = first_name + ' ' + last_name
        self.initials = first_name[0] + '.' + last_name[0] + '.'
