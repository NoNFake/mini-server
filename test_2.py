import random as rnd

word = "привет"
cenc = "*"


n: int = len(word)

word = word.replace(rnd.choice(word), cenc)
print(word)
