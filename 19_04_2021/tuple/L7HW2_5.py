first_sentence = input("Input first sentence: ")
second_sentence = input("Input second sentence: ")
first_set = set()
second_set = set()
sum_set = set()
for item in first_sentence:
     if ord(item) in  range(97,123):
        first_set.add(item)
        sum_set.add(item)
     elif ord(item) in  range(65,91):
        first_set.add(item)
        sum_set.add(item)
for item in second_sentence:
     if ord(item) in  range(97,123):
        second_set.add(item)
        sum_set.add(item)
     elif ord(item) in  range(65,91):
        second_set.add(item)
        sum_set.add(item)
print("First set:",sorted(first_set))
print("Second set:",sorted(second_set))
print("First and second set:",sorted(sum_set))
