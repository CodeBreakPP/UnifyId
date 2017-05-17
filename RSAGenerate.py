
from fractions import gcd
import requests
import sys


def randint(mini,maxi):
    a=mini
    while True:
        length=len(str(maxi))
        r=requests.get('https://www.random.org/strings/?num='+str(length)+'&len=1&digits=on&format=plain&rnd=new')
        a=int(''.join(r.text.split('\n')))
        if a>=mini and a<=maxi:
            break
    return a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def is_probable_prime(n, trials = 5):
    assert n >= 2

    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2 ** s * d == n - 1)
 
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(trials):
        a = randint(2, n)
        if try_composite(a):
            return False
    return True

p,q=1,1

while True:

    r = requests.get('https://www.random.org/strings/?num=10&len=10&digits=on&format=plain&rnd=new')
    a=r.text.split('\n')
    p=int(''.join(a))

    if p<3:
        continue

    if is_probable_prime(p):
        break

while True:

    r = requests.get('https://www.random.org/strings/?num=10&len=10&digits=on&format=plain&rnd=new')
    a=r.text.split('\n')
    q=int(''.join(a))
    if q<3:
        continue

    if is_probable_prime(q):
        break
    
n=p*q
phi=(p-1)*(q-1)


e,i = 0,2
while i<phi:
    if gcd( i, phi ) == 1:
        e = i
        break
    i+=1

d=modinv( e, phi )

print "* Public Key(n,e) = (" + str(n) + "," + str(e) + ")"
print "* Private Key(n,d) = (" + str(n) + "," + str(d) + ")"
