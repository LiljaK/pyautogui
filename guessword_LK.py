import random

words = ["apple","computer","pen","girl","sticker"]

hint1 = ["fruit","technology","writing utensel","Gender","sticky"]

hint2 = ["Comes from tree","key board","uses ink","pink","often used to decorate computers"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help.")
    guess = input()

    if guess ==secretword:
        print("you win!")
        break
elif guess == "hint1":
    print(   hint1[number]   )

elif guess == "hint2":
    print(   hint2[number]   )

elif guess == "first letter":
    print(   secretword[-1]   )

elif guess == "last letter1":
    print(   secretword[-1]   )

elif guess == "give up":
    print("The last word was" + secretword  )
    break

else:
    counter +=1
