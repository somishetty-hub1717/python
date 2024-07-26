import random
ran=random.randint(1,)
chances=1
while chances>=1:
    guess=int(input())
    if guess==ran:
        print('congrats')
        break
    else:
        chances-=1
        continue
while chances>3:
    print("failed")
