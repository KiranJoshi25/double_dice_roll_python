from random import randint
def roll_a_dice():
    j = randint(1,6)
    k = randint(1,6)
    return j,k

roll1, roll2 = roll_a_dice()
print(roll1,roll2)