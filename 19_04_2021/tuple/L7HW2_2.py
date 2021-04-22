sentence_tuple = tuple(input("Input the sentence: "))
sentence = list(sentence_tuple)
for symb in sentence_tuple:
    if symb in "1234567890=/*+-":
        count = sentence.count(symb)
        if  count > 1:
            del_symb = sentence.index(symb)
            sentence.pop(del_symb)
print("Sentence original: ",str("".join(sentence_tuple)))
sentence_tuple = tuple(sentence)
print("Sentence without repeat symbols numbers: ",str("".join(sentence_tuple)))
