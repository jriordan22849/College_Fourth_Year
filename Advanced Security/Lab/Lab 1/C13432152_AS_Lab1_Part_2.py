'''
Advanced Security 
Lab 1
Jonathan Riordan
C13432152
Part 2
'''

def fence(p, k):
    fence = [[None] * len(p) for n in range(k)]
    rails = range(k - 1) + range(k - 1, 0, -1)
    for n, x in enumerate(p):
        fence[rails[n % len(rails)]][n] = x
    return [c for rail in fence for c in rail if c is not None]

def encryptR(p, k):
    return ''.join(fence(p, k))

def decryptR(c, k):
    rng = range(len(c))
    pos = fence(rng, k)
    return ''.join(c[pos.index(k)] for k in rng)

message = "hello"
key = 2

encrypted_message = encryptR(message, key)
print('Encrypted message is: ' + encrypted_message)
print('Decrypted message is: ' + decryptR(encrypted_message, key))