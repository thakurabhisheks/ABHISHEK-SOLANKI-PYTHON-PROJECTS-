import random

def check(comp, user):
    if comp == user:
        return 0

    if(comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1

comp = random.randint(0, 2)
user = int(input("0 for rock, 1 for paper and 2 for scissor:  \n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if score == 0:
    print("thats not so good It's Draw.")
elif score == -1:
    print("Oh! You Loose.")
else:
    print("Yay You Won.")
