'''
    Advanced Security
    Student Name: Jonathan Riordan
    Student ID: C13432152
    
    Lab 3 - Part 2
    
    Output 
    Length of plaintext: 16
    Plaintext: AAAABBBBAAAABBBB
    Cipher Text: aac823f6bbe58f9eaf1fe0eb9ca7eb08
    Decrypted: AAAABBBBAAAABBBB
'''

from Crypto.Cipher import DES

key = '12345678'
message = "AAAABBBBAAAABBBB"
iv = '00000000'

obj = DES.new(key, DES.MODE_CBC,iv)

print "Length of plaintext: " + str(len(message))
ciphertext = obj.encrypt(message)
cp = ciphertext.encode("hex")

print "Plaintext: " + message
print "Cipher Text: " + cp

obj = DES.new(key, DES.MODE_CBC,iv)
print "Decrypted: " + obj.decrypt(ciphertext)
