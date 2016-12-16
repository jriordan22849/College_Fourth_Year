'''
    Advanced Security
    Lab 1
    Jonathan Riordan
    C13432152
    
    Part 1
'''

def getMessage():
	input_variable = raw_input("Enter your message: ")
	return input_variable

def caesar(s,k,decrypt=False):
	if decrypt: k=26-k
	r=""
	for i in s:
		if(ord(i) >= 65 and ord(i) <= 90):
			r += chr((ord(i) - 65 + k) % 26 + 65)
		
		elif (ord(i) >= 97 and ord(i) <= 122):
			r += chr((ord(i) - 97 + k) % 26 + 97)
			
		else:
			r += i
		
	return r

def encrypt(p,k):
	return caesar(p,k)
		
def decrypt(c,k):
	return caesar(c,k,True)

message = getMessage()		
key = 1
encrypted_message = encrypt(message, key)
print('Encrypted message is: ' + encrypted_message)
print('Decrypted message is: ' + decrypt(encrypted_message, key))
