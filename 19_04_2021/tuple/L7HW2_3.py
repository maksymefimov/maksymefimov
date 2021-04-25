sentence = input("Input the sentence: ")
num = set()
let_upe = set()
let_low = set()
for item in sentence:
    if ord(item) in range(48,58):
        num.add(int(item))
    elif ord(item) in  range(97,123):
        let_low.add(item)
    elif ord(item) in  range(65,91):
        let_upe.add(item)
num_set ={1,2,3,4,5,6,7,8,9,0}
num = num_set.difference(num)
print(sorted(num))
print(sorted(let_low))
print(sorted(let_upe))


