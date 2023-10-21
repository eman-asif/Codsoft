from random import randint
a = int(input('Enter length of password: '))
b = int(input('Enter the security level of password 1:low 2:medium 3:strong'))
s1 = 'qwertyuiopasdfghjklzmxncbvQWEARSFDTGYHZBXNCMVJHMKLOIP'
s2 = 'qwertyuiopasdfghjklz1234567890mxncbvQWEARSFDTGYHZBXNCMVJHMKLOIP'
s3 = 'qwert!@#$%yuiopasdfg^&*()_+]:"><.,/hjklz1234567890mxncbvQWEARSFDTGYHZBXNCMVJHMKLOIP'
s = ''
if b == 1:
    
    for i in range(a):
        c = randint(0,len(s1)-1)
        s += s1[c]
elif b == 2:
    
    for i in range(a):
        c = randint(0,len(s2)-1)
        s += s2[c]

elif b == 3:
    
    for i in range(a):
        c = randint(0,len(s3)-1)
        s += s3[c]
else:
    print('Invalid choice')
print(s)