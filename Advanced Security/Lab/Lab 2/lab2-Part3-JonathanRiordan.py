'''
	Advanced Security
	Lab 2
	Jonathan Riordan
	C13432152
	
	Part 3
	Output 
	Length of plain text: 175
Length of key: 8

I shall (from now on) select and take the ingots individually in my own yard, and I shall exercise against you my right of rejection because you have treated me with contempt.

Key: PASSWORD

xszshzwudmfgscevtlwupoegiacwpvvlcgglowegxvavqoconifeucnqnajvwbulhhsdhsohgcakaoxdxnkluclpnraydhfigebwyhzrcbwuwijhnomzwjvwgeslardhlilzycewtmhl

'''
alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

plainText = "I shall (from now on) select and take the ingots individually in my own yard, and I shall exercise against you my right of rejection because you have treated me with contempt."



key = "PASSWORD"
keyPositions = []



def encrypt(cipher,k):
	cipherText = ""
	ix = 0
	counter = 0
	remainder = 0
	lengthOfPlain = len(plainText)
	normallText = ""
	print "Length of plain text: " + str(lengthOfPlain)
	
	lenfthOfKey = len(k)
	print "Length of key: " + str(lenfthOfKey)
	
	#get position for each letter in the key. Save the values into an array.
	j = 0
	for i in key:
		
		if i in alphaUpper:
			position = alphaUpper.index(i)
			keyPositions.insert(j,position)
			j +=1
	
	#Remove any spaces or commas,full stops etc from the string
	for i in plainText:
		if i in alphaLower:
			#Get plain text letter postion
			positionPlain = alphaLower.index(i)
			normallText += i
			
		if i in alphaUpper:
			#Get plain text letter postion
			positionPlain = alphaUpper.index(i)
			normallText += i
		
	#Get the position of plainttext and position of each letter in the key and shift to get cipher text
	for i in normallText:
		if i in alphaLower:
			#Get plain text letter postion
			positionPlain = alphaLower.index(i)
			
			shift = positionPlain + keyPositions[counter]
			if shift > 25:
				rem = shift - 26
				shift = rem
			cipherText += alphaLower[shift]
			
			
		if i in alphaUpper:
			#Get plain text letter postion
			positionPlain = alphaUpper.index(i)
			shift = positionPlain + keyPositions[counter]
			if shift > 25:
				rem = shift - 26
				shift = rem
			cipherText += alphaLower[shift]
		counter += 1
		
		if counter > 7:
			counter = 0
			
	return cipherText
	

		
		
	
	

cipherText = encrypt(plainText, key)
print "\n" +plainText
print "\nKey: " + key
print "\n" + cipherText
