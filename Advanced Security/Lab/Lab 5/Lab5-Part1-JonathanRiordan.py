'''
    Advanced Security
    Student Name: Jonathan Riordan
    Student ID: C13432152
    
    Lab 5 - Part 1
'''
print "******************* Part 1 *******************"
m = 11 * 19
xi = 9

def rng():
    global xi
    xi = (xi * xi) % m
    return xi
    
for i in range(12):
    print rng()
