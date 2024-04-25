from Cryptodome.PublicKey import ElGamal as eg
from Cryptodome.Random import get_random_bytes,random

# TODO make 2048 bit modulus p and generator g
# i used 512 bits because 2048 bit generation did not complete in ~20 minutes
p = 11774363152266578095067526258816830539166139106121849415818805169740043699372268857521995275805757855836228222867569659145695568012997698531776585688862219
g = 2534890524550132494481097005281920111219579664822426722657432332577436305162772648334556738057313044668101379845453788943682939971615935369166151340598061

def keyGen() : # makes random sk and pk within group
    sk = random.randrange(1, p - 1)
    return eg.construct((p, g, pow(g, sk, p), sk))

def encrypt(egKey, message:int) :
    y = random.randrange(1, p - 1)
    s = pow(egKey.y, y, p)
    c1 = pow(g, y, p)
    c2 = (message * int(s)) % (p)
    return (c1,c2)

def decrypt(egKey, ct) :
    c1, c2 = ct
    s = pow(c1, int(egKey.x), p)
    sInv = pow(s, p-2, p)
    m = (c2 * sInv) % p
    return m

egKey = keyGen()
ct = encrypt(egKey, 12345678910)
m = decrypt(egKey, ct)
print(m)
