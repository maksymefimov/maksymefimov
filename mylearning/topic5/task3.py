num = input("Input the number: ")
num_index=len(num)
for i in range(len(num)):
    num_index -= 1
    if len(num)-2 < num_index:
        num_print = num[num_index]
    else:num_print += num[num_index]
print("Reverse number: %s" % num_print)
     
