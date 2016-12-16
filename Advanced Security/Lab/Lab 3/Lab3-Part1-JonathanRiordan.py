'''
Advanced Security
Student Name: Jonathan Riordan
Student ID: C13432152

Lab 3 - Part 1

Output 
Length of plaintext: 16
19ff4637bb2fe77c19ff4637bb2fe77c
AAAABBBBAAAABBBB

'''

from Crypto.Cipher import DES

key = '12345678'

obj = DES.new(key, DES.MODE_ECB)
message = "AAAABBBBAAAABBBB"
print "Length of plaintext: " + str(len(message))
ciphertext = obj.encrypt(message)
cp = ciphertext.encode("hex")

print "Key: " + key
print "Cipher text: " + cp

obj = DES.new(key, DES.MODE_ECB)
print "Plaintext: " +obj.decrypt(ciphertext)
