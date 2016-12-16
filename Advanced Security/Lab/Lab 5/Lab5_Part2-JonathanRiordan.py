'''
	Advanced Security
	Student Name: Jonathan Riordan
	Student ID: C13432152
	
	Lab 5 - Part 2
'''

from RandomnessTests import RandomnessTester

m = 11*19
xi = 9

def rng():
	global xi
	xi = (xi*xi) % m
	print(str(xi))
	return xi


bitstr = ""
for i in range(12):
	bitstr += bin( rng() )[-1:]

	
rng_tester= RandomnessTester(None)
p = rng_tester.monobit(bitstr)
print("p value ")
print(p)




