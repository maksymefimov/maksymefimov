##Створіть словник, в якому ключі – це числа, а значення – їх рядкова
##інтерпретація. Напишіть програму, що перетворює цей словник, в якому
##ключами будуть рядки а значеннями - числа.
print()
key_num = {}
for key in range(5):
    key_num[key] = str(key)
print("Dictinary original: ",key_num)
key_num = {v: k for k,v in key_num.items()}
print("Dictinary revers: ",key_num)
