##3. У змінній записаний текст. Словом вважається послідовність непорожніх символів,
##які йдуть підряд, слова розділені одним або більше пробілом.
##Програмно створіть словник, в якому ключами є слова з речення, а значеннями –
##кількість входження в речення.


def sentence():
    sentence_dict = {}
    sentence = input("Input sentence: ")
    sentence = sentence.split()
    for item in sentence:
        sentence_dict[item] = sentence.count(item)
    print()
    print("Dictionary from sentence:")
    for key,value in sentence_dict.items():
        print(f'Keys:{key:10s} = Counts:{value}')
    print()
    sentence_dict = sentence_dict.clear()
        

def main():
    while True:
        print("Menu:")
        print("1.Сreate dictionary from setence.")
        print("2.Exit")
        choose = input("Input your choice(number): ")
        if choose == '1' :
            sentence()
        elif choose == '2' :
            break
        else:
            print("Unknown choice!!!")
            

if __name__ == "__main__":
    main()
    
                                       
        
        
        

 

