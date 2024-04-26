from elGamal import ElGamal as eg
from Cryptodome.Random.random import randrange

# encryption, decryption test
message = 12345678910
cipher = eg()
ct = cipher.encrypt(message)
result = cipher.decrypt(ct)
print(result)
print(message == result)

# secret key share test
shares = []
groupSize = 5

pkGen = 1
for i in range(groupSize) :
    cipher = eg()
    pkGen = cipher.multG(pkGen)
    shares.append(int(cipher.key.x))

sk = sum(shares)
pk = pow(cipher.g, sk, cipher.p)

print(f'Real key is {"not" if pk!=pkGen else ""}equal to generated key.\nReal:\n{pk}\nGenerated:\n{pkGen}')

