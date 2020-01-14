from numpy import *
from random import randint
file=open('chirac.txt', 'r')
data = file.read()
l=290*' '
while len(l)>280:
    k=randint(0,len(data)-1)
    while data[k]=='.' or data[k]=='?' or data[k]=='!':
        k=randint(0,len(data)-1)
    k0=k
    l=""
    while data[k]!='.' and data[k]!='.' and data[k]!='.':
        l=data[k]+l
        k-=1
    k=k0+1
    while data[k]!='.' and data[k]!='.' and data[k]!='.':
        l=l+data[k]
        k+=1
    l=l+data[k]
    l=l+' ACAB cependant.'
print(l)
        