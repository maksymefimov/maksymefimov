##Задано символьний рядок,. Розробити програму, яка знаходить групи цифр,
##записаних підряд, і вилучає із них всі початкові нулі, крім останнього, якщо за
##ним знаходиться крапка. Друкує модифікований масив по сорок символів у рядку.
sentence = list(input("Input a sentence: "))
counter = 0
for i in reversed(sentence):
    if i  == '.':
       counter = 1
    if counter == 1: 
        if i == '0' and sentence[sentence.index(i)-1] == 0:
           print('1',index)
           sentence.pop(sentence.index(i))
        
       

print(sentence)
        
#недоделано
                          
   
