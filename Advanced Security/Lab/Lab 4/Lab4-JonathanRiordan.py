#!/usr/bin/python
'''
	Advanced Security
	Student Name: Jonathan Riordan
	Student ID: C13432152
	
	Lab 4 - Part 1 && Part 2
	
	Output
	
	Plain text: AAAABBBBCCCCDDDDAA
	32
	Cipher text: 43d3215c92a75a1478fcf9cb950d20dbcb92e17929013822cf6dde42d50346b8
	64
	Decrypted: AAAABBBBCCCCDDDDAA00000000000001
	Decrypted with no padding: AAAABBBBCCCCDDDDAA
	******************* Part 2 *******************
	AAAABBBBCCCCDDDDAA
	
	This is the solved plaintext:AAAABBBBCCCCDDDDAA
	
	
	The file wont compile if i put the results in the comment section aboove because of the characters, but it does compile now and the output can be seen. The user gets the output of all the keys in the dictionary file and can see the plaintext. 
	
'''

import base64

from Crypto.Cipher import AES

print "******************* Part 1 *******************"
def addPadding(plaintext, length):    
	i = 0
	j = 0
	
	one = "1"
	zero = "0"
	block_size = 32
	temp = block_size - 1
	numOfPadding = block_size - length
	while i < block_size:
		
		if i > length:
			plaintext += "0"
		if i == block_size - 1:
			plaintext += "1"
		i += 1
		
	return plaintext
	
	
	


def removePadding(cipher, len):
	i = 0
	message = ""
	block_size = 16
	
	numOfPadding = block_size - len
	length = block_size - numOfPadding
	
	while i < length:
		message += cipher[i]
		i += 1
		

	return message


key = '1234567812345678'
plainText = "AAAABBBBCCCCDDDDAA"
ciphertext = ""
encoded = ""

length = len(plainText)

print "Plain text: " + plainText


ciphertext = addPadding(plainText, length)
obj = AES.new(key, AES.MODE_ECB)
print len(ciphertext)

cp = obj.encrypt(ciphertext)
cp = cp.encode("hex")
print "Cipher text: " + cp
print len(cp)


dec = cp.decode("hex")

obj = AES.new(key, AES.MODE_ECB)
dec =  obj.decrypt(dec)
print "Decrypted: " + dec

decrypt = removePadding(dec,length)
print "Decrypted with no padding: " + decrypt

'''
Part 2
'''

print "******************* Part 2 *******************"

file = open("dictionary.txt", "r")
dictionary = []

for line in file:
	if (len(line) >= 17):
		dictionary.append(str(line[:-1]))
	else:
		dictionary.append(str(line))
file.close()

cipherPart2 = "43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD"
for i in dictionary:
	key = i;
	dec = cipherPart2.decode("hex")
	obj2 = AES.new(i, AES.MODE_ECB)
	dec = obj2.decrypt(dec)
	print removePadding(dec,len(plainText) )