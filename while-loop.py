import random
guess = ""
answer = random.randrange(1,10)

while guess != answer:
    guess = int(input("what 6is you guess!:"))
    if guess > answer:
        print("the answe is lower")
    elif guess < answer:
        print("the answe is higher")
    else:
        print("correct anser")