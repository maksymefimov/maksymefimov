sentence = tuple(input("Input the sentence: "))
string_low = "eyuioa"
string_up = "qwrtpsdfghjklzxcvbnm"
low = "" 
up = ""
for symb in sentence:
        if symb in string_low:
            low += symb
        elif symb in string_up:
            up += symb

print("Vowels: ",", ".join(low))
print("Consonants: ",", ".join(up))
print(sentence)
