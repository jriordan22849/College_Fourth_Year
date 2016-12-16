# Diffie-Helman

p = 23    # publicly known
g = 5    # publicy known 

a = 6    # only Allice
b = 15    # only Bob knows this

def mod(num, g):
    A = (g ** num) % p
    return A

 
numberA = mod(a,g)
numberB = mod(b, g)


s = mod(a, numberB)
s2 = mod(b, numberA)

print "Publicly shared prime ", p
print "Publicly shared base", g

print "-------------------"
print "Alice sends over public channel: ", numberA
print "Bob sends over public channel: ", numberB
print "-------------------"

print "Alice shared secret ", s
print "Bob shared secret ", s2


