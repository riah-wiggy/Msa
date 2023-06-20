#import random library
import random

#generate random nuber
random_number = random.randint(0, 10)

print(random_number)

for rand_number in range(10000):
    print(" "*(rand_number%50), end="")
    print(random.randint(0, 1000))