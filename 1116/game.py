import random

upper = 100
under = 1

ans = random.randint(under, upper)

for i in range(5):

    guess = int(input("please input a number: ")) 

    if guess < ans:
        under = guess
    elif guess > ans:
        upper = guess
    else:
        print("BOOM!")
        break


    print(under, upper)
