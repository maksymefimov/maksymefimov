##2. Створіть словник, ключами є слова, а значеннями – список слів-синонімів до нього.
##Програма отримує на вхід кількість слів N. Далі користувач вводить слова-ключі та
##відповідні йому синоніми.
##Передбачити:
##1) на запит (слово) користувача вивести список синонімів;
##2) користувач вводить речення, в якому є слова (ключі, що містяться в словнику).
##Замінити їх синонімами та вивести речення на екран.
def create():
    while True:
        key_word = input("Input key word to create: ")
        if key_word == '0':
            print()
            break
        synonyms = input("Input synonyms for %s with space: " % key_word)
        synonyms = synonyms.split()
        synonyms_dict [key_word] = synonyms
        print()


def search():
    while True:
        key_word = input("Input key word to search: ")
        if key_word == '0':
            print()
            break
        if key_word in synonyms_dict:
            print("Synonyms for %s : %s"%(key_word,synonyms_dict[key_word]))
            print()
        else:
            print("Key word not found")
            print()

def sentence():
    import random
    while True:
        sentence = input("Input sentence: ")
        if sentence == '0':
            print()
            break
        sentence = sentence.split()
        for item in sentence:
            if item in synonyms_dict:
                random_synonym = random.choice(synonyms_dict[item])
                index_word = sentence.index(item)
                sentence[index_word] = random_synonym
        print("Changed sentence: " , ' '.join(sentence))
        
        

def main():
    global synonyms_dict
    synonyms_dict = {}
    while True:
        print("Menu:")
        print("1.Create key word with synonyms.")
        print("2.Search word with synonyms in dictinary.")
        print("3.Sentence with synonyms.")
        print("4.Print synonyms dictionary .")
        print("5.Exit")
        print("If you want to exit from function enter 0 !!!")
        choose = input("Input your choice(number): ")
        if choose == '1' :
            create()
        elif choose == '2' :
            search()
        elif choose == '3' :
            sentence()
        elif choose == '4' :
            print()
            print("Dictionary:")
            for key,value in synonyms_dict.items():
                print(f'{key:10s} = {value}')
            print()
        elif choose == '5' :
            break
        else:
            print("Unknown choice!!!")
            

if __name__ == "__main__":
    main()
    
                                       
        
        
        

 

