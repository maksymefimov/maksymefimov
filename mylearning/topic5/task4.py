import random
num_random = random.randint(0,100)
#print(num_random)
for i in range(1,11):
    num_random2 = int(input("Attempt %s!\n\
Enter a number that you think is random: " % i))
    if num_random2 > num_random:
        print("The number entered is more than random!!!")
    elif num_random2 < num_random:
        print("the number entered is less than random!!!")
    elif num_random2 == num_random:
        print("Congratulations you guessed the random number !!!")
        break
if num_random != num_random2:
    print("You lost!!!")
    print("Random number: %d !!!"%num_random)
print("The End!!!")
