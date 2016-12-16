'''
	Advanced Security
	Lab 2
	Jonathan Riordan
	C13432152
	
	Part 1 
	
	Key = -3
	
	Message = "And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit of his writings as fully as he could desire; for my desire has been no other than to deliver over to the detestation of mankind the false and foolish tales of the books of chivalry, which, thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall for ever. Farewell."
	
	
	Cipher text: Xka F pexii objxfk pxqfpcfba, xka molra ql exsb ybbk qeb cfopq tel exp bsbo bkglvba qeb corfq lc efp tofqfkdp xp criiv xp eb zlria abpfob clo jv abpfob exp ybbk kl lqebo qexk ql abifsbo lsbo ql qeb abqbpqxqflk lc jxkhfka qeb cxipb xka cllifpe qxibp lc qeb yllhp lc zefsxiov, tefze, qexkhp ql qexq lc jv qorb Alk Nrfulqb, xob bsbk klt qlqqbofkd, xka alryqibpp alljba ql cxii clo bsbo. Cxobtbii.

'''

key = -3
message = "And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit of his writings as fully as he could desire; for my desire has been no other than to deliver over to the detestation of mankind the false and foolish tales of the books of chivalry, which, thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall for ever. Farewell."

alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(plaintext, key, arraylower, arrayupper): 
	cipherText = ""
	position = 0
	temp = 0
	remainder = "0"
	for i in plaintext:
		if i in arraylower:

			position = arraylower.index(i)
			temp = position + key
			if temp > 25:
				remainder = temp - 26
				temp = remainder
			if temp < 0:
				remainder = temp
				temp = 26
				temp = temp + remainder
			cipherText += arraylower[temp]
		if i in arrayupper:
			position = arrayupper.index(i)
			temp = position + key
			if temp > 25:
				remainder = temp - 26
				temp = remainder
			if temp < 0:
				remainder = temp
				temp = 26
				temp = temp + remainder
			cipherText += arrayupper[temp]
			
		if i == ",":
			cipherText += ","
		if i == ".":
			cipherText += "."
		if i == "!":
			cipherText += "!"
		if i == " ":
		    cipherText += " "

			
		position = 0
		temp = 0
		remainder = 0
		
	return cipherText

cipherText = encrypt(message, key,alphaLower, alphaUpper )
print cipherText





