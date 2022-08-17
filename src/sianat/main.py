import random
'''
w = 'salam khoubi chetori'
c = 0
for ch in w:
    if ch == 'a' or ch == 'e' or ch == 'o' or ch == 'u' or ch == 'i':
        c += 1
        print(ch ,end = ' ')
print(c)


for i in range(1,4):
    for j in range(i):
        print(j+1,end = ' ')
    print()


r = random.randrange(0,10)
#print(r)
while True:
    n = int(input('guess number:'))
    if r < n:
        print('r is smaller')
    elif r > n:
        print('r is grather')
    else:
        print('correct')
        break

'''

n = random.randrange(0,10)
flag = 'no'
while flag == 'no':
    a = int(input('enter number:'))
    if a < n :
        print('>')
    elif a > n :
        print('<')
    else:
        print('correct')    
        flag = 'yes'