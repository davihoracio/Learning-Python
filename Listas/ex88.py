import random
import time
r = int(input('Quantos números você quer sortear? '))
li = []
for c in range(r):
    li.append(random.sample(range(1, 61),6))
    print(li)
    li.clear()
    time.sleep(2)