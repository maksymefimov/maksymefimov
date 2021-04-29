##Задано символьний рядок,. Розробити програму, яка знаходить групи цифр,
##записаних підряд, і вилучає із них всі початкові нулі, крім останнього, якщо за
##ним знаходиться крапка. Друкує модифікований масив по сорок символів у рядку.
sentence = list(input("Input a sentence: "))
counter = 0
flag = 0
for i in reversed(range(0,len(sentence))):
    if sentence[i]  == '.':
        flag = 1
    if sentence[i] == '0' and flag == 1 :
        counter += 1
    if ord(sentence[i]) in range(97,123) and flag == 1:
        counter -= 1
        index_slice = i+1
        sentence = sentence[:index_slice] + sentence[index_slice + counter:]
        flag = 0
        counter = 0
    elif sentence[i] in "123456789" and flag == 1:
        flag = 0
        counter = 0
print(''.join(sentence))
        

                          
   
