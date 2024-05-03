from elGamal import ElGamal as eg
from Cryptodome.Random import random
from client import send
from server import receive

groupSize = 3
partNum = 1
cipher = eg()
ip = "192.168.0.1"

pkShare = receive()
send(cipher.mult(pkShare), ip)
pk = receive()
cipher.setPK(pk)

vector = receive()
while vector != None :
    cipher.shuffle(vector)
    send(vector, ip)

    quotient = receive()
    send(cipher.blindVector(quotient), ip)
    blinded = receive()
    send(blinded, ip)

    decryptionShares = receive()
    sendShares = list()
    for i in range(groupSize) :
        decShare = cipher.decShare(blinded[i])
        sendShares.append((decShare * decryptionShares[i]) % cipher.p)
    
    send(sendShares, ip)
    vector = receive()
send(None, ip)

shuffled = receive()
blindFactor = random.randrange(1, cipher.p - 1)
encFactor = cipher.encrypt(blindFactor)
c1blind = (shuffled[partNum][0] * encFactor[0]) % cipher.p
c2blind = (shuffled[partNum][1] * encFactor[1]) % cipher.p
shuffled[partNum] = (c1blind, c2blind)
send(shuffled, ip)

assignments = receive()
send(assignments, ip)

assnDecShares = receive()
for i in range(groupSize) :
    share = cipher.decShare(assignments[i])
    assnDecShares[i] = (assnDecShares[i] * share) % cipher.p

send(assnDecShares, ip)
plainAssignments = receive()
gRecipient = plainAssignments[partNum] // blindFactor
recipient = cipher.log(gRecipient)
send(plainAssignments, ip)
print(recipient)