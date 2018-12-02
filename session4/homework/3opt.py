# a
from random import choice, randint

words = "champion"
characters = list(words)

for _ in range(len(characters)):
    i = randint(0, len(characters) - 1)
    ch = characters[i]

    print(ch, end=" ")

    characters.pop(i)

print()

user_guess = input("Your guess? ")
if user_guess == words:
    print("True")
else:
    print(":(")

#b
from random import randint

word_list = ["hexagon", "meticulous", "champion"]


i = randint(0, (len(word_list) - 1))
a = word_list[i]
word = word_list[i]
    
for _ in range(len(a)):               
    j = randint(0, (len(a) - 1))
    a = list(a)
    ch = [j]
    print(ch,end=" ")
    a.pop(j)
print()

user_guess = input("Your answer: ")
if user_guess == word:
    print("True, you are great!")
else:
    print("cực ngu") 