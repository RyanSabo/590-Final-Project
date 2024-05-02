from elGamal import ElGamal as eg
from Cryptodome.Random.random import randrange
from copy import deepcopy

# encryption, decryption test
message = 12345678910
cipher = eg()
ct = cipher.encrypt(message)
result = cipher.decrypt(ct)
print(result)
print(message == result)

# secret key share test
shares = []
ciphers = []
groupSize = 5

pkGen = 1
for i in range(groupSize) :
    cipher = eg()
    pkGen = cipher.mult(pkGen)
    shares.append(int(cipher.x))
    ciphers.append(cipher)

sk = sum(shares) % (cipher.p -1)
pk = pow(cipher.g, sk, cipher.p)

#print(pow(cipher.g, cipher.p, cipher.p))
#print(pow(cipher.g, 1, cipher.p))
print(f'Real key is {"not" if pk!=pkGen else ""}equal to generated key.\nReal:\n{pk}\nGenerated:\n{pkGen}')

# re-encryption shuffle test
master = eg()
master.setSK(sk)

for ciph in ciphers :
    ciph.setPK(pk)
vector = master.vector(groupSize)


originalVector = deepcopy(vector)
for ciph in ciphers :
    ciph.shuffle(vector)

quotient = master.divide(originalVector,vector)
quotient = master.blindVector(quotient)
for i in range(groupSize) :
    vector[i] = master.decrypt(vector[i])
    originalVector[i] = master.decrypt(originalVector[i])
    quotient[i] = master.decrypt(quotient[i])

print(quotient)