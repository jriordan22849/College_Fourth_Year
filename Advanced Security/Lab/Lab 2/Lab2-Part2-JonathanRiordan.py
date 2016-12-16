'''
	Advanced Security
	Lab 2
	Jonathan Riordan
	C13432152
	
	Part 2
	
	Output: 
	PlainText: It would seem that as he examined the several possibilities a suspicion crossed his mind the memory of how he himself had behaved in earlier days made him ask whether     someone might be hiding her from the world
    Key is 13
'''
alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cipherText = "Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or uvqvat ure sebz gur jbeyq"

def decrypt(cipher,k):
	plaintText = ""
	position = 0
	temp = 0
	remainder = "0"
	for i in cipher:
		if i in alphaLower:
			position = alphaLower.index(i)
			position += k
			
			if position > 25:
				remainder = position - 26
				position = remainder
				
			if position < 0:
				remainder = position
				position = 26
				position = position + remainder	
			plaintText += alphaLower[position]
			
		if i in alphaUpper:
			position = alphaUpper.index(i)
			position += k
			
			if position > 25:
				remainder = position - 26
				position = remainder
				
			if position < 0:
				remainder = position
				position = 26
				position = position + remainder	
			plaintText += alphaUpper[position]
			
		if i == " ":
			plaintText += " "
		position = 0
		temp = 0
		remainder = "0"
				 
				
	return plaintText
	
	
	
i = 0
key = 0
while i <= 26:
	

	plaintText = decrypt(cipherText, key)
	if "the" in plaintText or "in" in plaintText:
		print "PlainText: " + plaintText
		print "Key is " + str(key)
		break;

	i += 1
	key = key + 1

