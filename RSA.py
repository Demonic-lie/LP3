import math

def coprimes(a):
    l = []
    for x in range(2, a):
        if math.gcd(a,x) == 1 and pow(x, -1, phi)!= None:
            l.append(x)
    for x in l:
        if x == pow(x, -1, phi):
            l.remove(x)
    return l


def encrypt_block(m):
    return (m ** e % n)

def decrypt_block(m):
    return (m ** d % n)


def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])



def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
    

if __name__ == "__main__":
    p = int(input("Enter prime p "))
    q = int(input('Enter prime q '))

    print("Chosen prime no. "+ str(p)+" and " + str(q))

    n = p * q

    phi = (p-1) * (q-1)

    print("n = p*q = " + str(n))
    print("Euler's Function: " + str(phi))

    print('choose e from given coprime no. ')
    print(str(coprimes(phi)))

    e = int(input())

    d = pow(e,  -1, phi)

    print("Your public key pair is : e = "+ str(e) + " n = " + str(n))
    print("Your Private key pair is : d = " + str(d) + 'n = '+ str(n))

    s = input("Enter a string ")
    print("\nPlain message : " + s )

    enc = encrypt_string(s)
    print("Encrypted string is : " + enc)

    
    dec = decrypt_string(enc)
    print("Encrypted string is : " + dec)