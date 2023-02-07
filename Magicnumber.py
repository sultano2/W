import random
magic_number=random.randint(1,100)
i=5
while i>0:
    i=i-1
    guess=int(input("what is the Magic Number (between 1 and 100): "))
    if guess>magic_number:
        print(f"the number is lower. you have {i} guesses left")
    if guess<magic_number:
        print(f"the number is higher. you have {i} guesses left")
    if guess==magic_number:
        print("noice, u got it!-------------- thx for playing")
        break
    elif i==0:
        print("-----------------------------------------------------------------------Maybe next time, Thx for playing unlucky guesser--------------------------------------------------------")
 
