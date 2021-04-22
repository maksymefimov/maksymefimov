def calcSum(strNums):
    list_nums = strNums.split()
    s = 0
    for i in list_nums:
        s += int(i)
    return sum(list_nums)
print("Please start to enter value string of numbers separated by space. #: stop input: ")
ans = "o"
total = 0
while ans != "#":
    strNums = input()
    if "#" in strNums:
        ans = "#"
        i = strNums.index('#')
        strNums = strNums[:i]
    sum_str = calcSum(strNums)
    print(sum_str)
    total += sum_str
print(total)
                    
