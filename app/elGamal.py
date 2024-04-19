from Cryptodome.PublicKey import ElGamal as eg
from Cryptodome.Random import get_random_bytes,random

# modulus and generator
p = 11774363152266578095067526258816830539166139106121849415818805169740043699372268857521995275805757855836228222867569659145695568012997698531776585688862219
g = 2534890524550132494481097005281920111219579664822426722657432332577436305162772648334556738057313044668101379845453788943682939971615935369166151340598061
length = 512

def keyGen() : # makes random sk and pk within group
    sk = random.randrange(1, p - 1)
    return eg.construct((p, g, pow(g, sk, p), sk))

def encrypt(egKey, message) :
    y = random.randrange(1, p - 1)
    s = pow(egKey.y, y, p-1)
    c1 = pow(g, y, p-1)
    c2 = (message * s) % (p - 1)
    return (c1,c2)

def decrypt(egKey, ct) :
    c1, c2 = ct
    sInv = int(pow(c1, p - int(egKey.x), p-1))
    m = (c2 * sInv) % (p - 1)
    m = m.to_bytes(100, byteorder='big')
    return str(m, encoding="utf-8")

egKey = keyGen()
ct = encrypt(egKey, 590)
m = decrypt(egKey, ct)
print(m)

# i just realized we're only encrypting integers for the actual protocol
# so maybe we can just input integers
# word that makes it a bit easier i think since we don't need to convert between types of stuff