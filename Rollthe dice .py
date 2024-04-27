import random
repeat = True
while repeat:
    print("You rolled",random.randint(1,6))
    print("Do you want to do it again? Yes/No")
    repeat = "Yes" in input()
