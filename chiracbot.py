import tweepy, time, sys
from numpy import *
from random import randint
file=open('chirac.txt', 'r')
data = file.read()
def gen():
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
    return(l)
        
        

INTERVAL = 60 * 60 * 24
auth = tweepy.OAuthHandler(c1, c2)
auth.set_access_token(c3, c4)

api = tweepy.API(auth)

while True:
    print("about to get ad...")
    ad = gen()
    api.update_status(ad)
    time.sleep(INTERVAL)
        
