import random

def randint(min = 0, max = 100):
    return int(random.random() * (max - min) + min)

print(randint())
print(randint(max = 50))
print(randint(min = 50))