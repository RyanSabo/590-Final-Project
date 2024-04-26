from Cryptodome.PublicKey import ElGamal as eg
from Cryptodome.Random import random


class ElGamal:
    def __init__(self) : # makes random sk and pk within group
        # TODO make 2048 bit modulus p and generator g
        # i used 512 bits because 2048 bit generation did not complete in ~20 minutes
        self.p = 11774363152266578095067526258816830539166139106121849415818805169740043699372268857521995275805757855836228222867569659145695568012997698531776585688862219
        self.g = 2534890524550132494481097005281920111219579664822426722657432332577436305162772648334556738057313044668101379845453788943682939971615935369166151340598061

        sk = random.randrange(1, self.p - 1)
        self.key = eg.construct((self.p, self.g, pow(self.g, sk, self.p), sk))

    def encrypt(self, message:int) : # ElGamal encryption
        y = random.randrange(1, self.p - 1)
        s = pow(self.key.y, y, self.p)
        c1 = pow(self.g, y, self.p)
        c2 = (message * int(s)) % self.p
        return (c1,c2)

    def decrypt(self, ct) : # ElGamal encryption
        c1, c2 = ct
        s = pow(c1, int(self.key.x), self.p)
        sInv = pow(s, self.p-2, self.p) # inverting by raising to p - 2
        m = (c2 * sInv) % self.p
        return m

    def mult(self, element, factor) : # raise
        return (factor * pow(int(self.g), int(self.key.x), int(self.p))) % self.p

    def multG(self, factor) : # if element is not specified, use generator g
        return self.mult(self.g, factor)
