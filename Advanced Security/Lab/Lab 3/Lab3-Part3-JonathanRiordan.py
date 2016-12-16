'''
    Advanced Security
    Student Name: Jonathan Riordan
    Student ID: C13432152
    
    Lab 3 - Part 3
    
    Output
    Plain text: ABCDEFGHIJK
    16
    Cipher text: 96de603eaed6256f20f2c43eb7cd8b67
    32
    Decrypted with padding: ABCDEFGHIJK00001
    Decrypted: ABCDEFGHIJK

'''
import base64

from Crypto.Cipher import DES


def addPadding(plaintext, length):    
    i = 0
    j = 0
    
    one = "1"
    zero = "0"
    block_size = 16
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


key = '12345678'
plainText = "ABCDEFGHIJK"
ciphertext = ""
encoded = ""

length = len(plainText)

print "Plain text: " + plainText


ciphertext = addPadding(plainText, length)
obj = DES.new(key, DES.MODE_ECB)
print len(ciphertext)

cp = obj.encrypt(ciphertext)
cp = cp.encode("hex")
print "Cipher text: " + cp
print len(cp)


dec = cp.decode("hex")

obj = DES.new(key, DES.MODE_ECB)
dec =  obj.decrypt(dec)
print "Decrypted with padding: " + dec

decrypt = removePadding(dec,length)
print "Decrypted: " + decrypt





