from elGamal import ElGamal as eg
from Cryptodome.Random import random
from client import send
from server import receive
import socket

groupSize = 3
partNum = 1
cipher = eg()
ip = "172.20.10.6"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50007))
s.bind((ip, 50007))

pkShare = receive(s)
send(cipher.mult(pkShare), s)
pk = receive(s)
cipher.setPK(pk)
send(pk, s)

vector = receive(s)
while vector != None :
    cipher.shuffle(vector)
    send(vector, s)

    quotient = receive(s)
    send(cipher.blindVector(quotient), s)
    blinded = receive(s)
    send(blinded, s)

    decryptionShares = receive(s)
    sendShares = list()
    for i in range(groupSize) :
        decShare = cipher.decShare(blinded[i])
        sendShares.append((decShare * decryptionShares[i]) % cipher.p)
    
    send(sendShares, s)
    vector = receive(s)
send(None, s)

shuffled = receive(s)
blindFactor = random.randrange(1, cipher.p - 1)
encFactor = cipher.encrypt(blindFactor)
c1blind = (shuffled[partNum][0] * encFactor[0]) % cipher.p
c2blind = (shuffled[partNum][1] * encFactor[1]) % cipher.p
shuffled[partNum] = (c1blind, c2blind)
send(shuffled, s)

assignments = receive(s)
send(assignments, s)

assnDecShares = receive(s)
for i in range(groupSize) :
    share = cipher.decShare(assignments[i])
    assnDecShares[i] = (assnDecShares[i] * share) % cipher.p

send(assnDecShares, s)
plainAssignments = receive(s)
gRecipient = plainAssignments[partNum] // blindFactor
recipient = cipher.log(gRecipient)
send(plainAssignments, s)
print(recipient)