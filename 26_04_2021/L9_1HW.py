##1. Створіть словник, зв'язавши його з змінною school, і наповніть його даними, які б
##відображали кількість учнів в десяти різних класах (наприклад, 1а, 1б, 2б, 6а, 7в
##тощо.). Дізнайтеся скільки людей в певному класі.
##Уявіть, що в школі відбулися зміни, додайте їх в словник:
##- В трьох класах змінилося кількість учнів;
##- В школі з'явилося два нових класи;
##- В школі розформували один з класів.
##Виведіть вміст словника на екран.
def school_gen(school_f):
    import random
    school_func = {}
    for l in range(0,3):
        if l == 0 :
            name = 'a'
        elif l == 1 :
            name = 'b'
        elif l == 2 :
            name = 'c'
        for i in range(1,12):
            school_func[str(i)+name] = random.randint(10,25)
    return school_func


def people_class():
    class_school = input("Input number of class: ")
    if class_school in school:
        print("%s class has %d students."%(class_school,school[class_school]))
        students = int(input("Input number of students(max.31): "))
        if students > 0 and students < 32:
            school[class_school] = students 
            print("%s class changed and he has %d students."%(class_school,school[class_school]))
        else:
            print("Incorrect value of students for class!!!")
    else:
        print("Class not exist!!!")


def new_class():
    number_class = input("Input a new number of class(max.11): ")
    if int(number_class) > 0 and int(number_class) < 12:
        letter_class = input("Input a letter of class(max.one letter a-z): ")
        if len(letter_class) > 1:
            return print("Incorrect input!!!Start again!!!")
        if ord(letter_class[0]) in range(97,123):
            student_class = int(input("Input a how many students in  class(max.31): "))
            if student_class > 0 and student_class < 32:
                school[number_class + letter_class] = student_class 
                print("%s class created and he has %d students."%(number_class + letter_class,school[number_class + letter_class]))
            else:
                return print("Incorrect input!!!Start again!!!")
        else:
            return print("Incorrect input!!!Start again!!!")    
    else:
        return print("Incorrect input!!!Start again!!!")

 
def delete_class():
    number_class = input("Enter the class name you want to delete: ")
    if number_class in school:
        student = school[number_class]
        school.pop(number_class)
        print("There are %d students left who need to be distributed among the class of similar %s !!!" % (student,number_class))
       
    else:
        return print("Class not exist!!!")

def main():
    global school
    school = {}
    school = school_gen(school)
    while True:
        print("Menu:")
        print("1.Сhange the number of people in the class.")
        print("2.Make new class.")
        print("3.Delete class.")
        print("4.Print shool dictionary of classes.")
        print("5.Exit")
        choose = input("Input your choice(number): ")
        if choose == '1' :
            people_class()
        elif choose == '2' :
            new_class()
        elif choose == '3' :
            delete_class()
        elif choose == '4' :
            for key,value in school.items():
                print(f'{key:3s} = {value}')
        elif choose == '5' :
            break
        else:
            print("Unknown choice!!!")
            

if __name__ == "__main__":
    main()
    
                                       
        
        
        

 

