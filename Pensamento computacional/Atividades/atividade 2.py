n = int(input('Qual o N? '))
li = list()
print('Digite os valores: ')
for c in range(0,n):
    li.append(int(input()))
op = int(input('Qual a op [0/1]? '))
a = int(input('Qual o A? '))
b = int(input('Qual o B? '))
if op == 0:
    s = li[a-1]+li[b-1]
    print(f'{li[a - 1]} + {li[b - 1]} = {s}')
if op == 1:
    p = li[a-1]*li[b-1]
    print(f'{li[a - 1]} * {li[b - 1]} = {p}')

