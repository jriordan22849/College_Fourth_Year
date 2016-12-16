'''
	Advanced Security
	Lab 2
	Jonathan Riordan
	C13432152
	
	Part 4
	
	Output YHWVTROIYUDQPSEBJATWPTFOXGFZWJZQLBGIOQCWELWLARBLSGRMPROCHEKEWRVNSOYRUVSNDCLJEBVRKPKIUMHYBEFSJRWUTMVLJGAYBEFLDSYDXMCHFASXBOJWLWFXXAPHFJSBNTZAJUKKWIXITHVBDUYZKIKWMEYLPZSGDRDVWBUWMEMMOUOLHTSAJGWUTMMMMZWXVLANEBXEJIPKTOBNDTZWNAVQFNFXICGOLHGSNSYXSTUQFBOXSFAKDSIPJNQJUVSUXNYZWJVGJSKWUSRPGOEZQBKLSGCREWTCDMWOAFVLSTGQQSFKIELZAMYDAEEIBGSNURGEPVVLWIPXFADOGAFUAOJZFSKRUVSSGPGOAFRQIODI    EWSXITGLDSZUKAVLFFOXSMGLDSIDSDVSUVSOADWJOWERUPQWJHWYCTGLDSGDXTCPTCWXIHWXQHLUJBAWPOQDXNYGJSMHWYQGDOGSDNLZAMNLQLNMWSPOITWJWBUPTRGLBDDSAY


THURSDAYJULYTENYEARSOFREIGNHAVINGBEENCOMPLETEDKINGPIODASSESMADEKNOWNTHEDOCTRINEOFPIETYTOMENANDFROMTHISMOMENTHEHASMADEMENMOREPIOUSANDEVERYTHINGTHRIVESTHROUGHOUTTHEWHOLEWORLDANDTHEKINGABSTAINSFROMKILLINGLIVINGBEINGSANDOTHERMENANDTHOSEWHOAREHUNTSMENANDFISHERMENOFTHEKINGHAVEDESISTEDFROMHUNTINGANDIFSOMEWEREINTEMPERATETHEYHAVECEASEDFROMTHEIRINTEMPERANCEASWASINTHEIRPOWERANDOBEDIENTTOTHEIRFATHERANDMOTHERANDTOTHEELDERSINOPPOSITIONTOTHEPASTALSOINTHEFUTUREBYSOACTINGONEVERYOCCASIONTHEYWILLLIVEBETTERANDMOREHAPPILY

key is FACEBOOKPASSWORD
'''
alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cipherText =  "Yhwvtroi, 28 Yudq 2016 - Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg, cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay"

key = "FACEBOOKPASSWORD"

keyPositions = []
plainPositions = []



def removeChar(plaintext):
    m = ""
    n = 0
    for i in plaintext:
		if i in alphaUpper:
			#Get plain text letter postion
			positionPlain = alphaUpper.index(i)
			m += alphaUpper[positionPlain]
				
		if i in alphaLower:
			#Get plain text letter postion
			positionPlain = alphaLower.index(i)
			m += alphaUpper[positionPlain]
    return m

def decrypt(cipher):
	lengthKey = len(key)
	j = 0
	k = 0
	counter = 0
	plain =""
	normal =""
	#Get key positions
	for i in key:
		if i in alphaUpper:
			position = alphaUpper.index(i)
			keyPositions.insert(j,position)
			j += 1
			

	#get ciphertext positions
	for i in cipher:
		if i in alphaUpper:
			#Get plain text letter postion
			positionPlain = alphaUpper.index(i)
			plainPositions.insert(k,positionPlain)
			k += 1
			
			shift = positionPlain - keyPositions[counter]
			
			if shift > 25:
				rem = shift - 26
				shift = rem
			if shift < 0:
				remainder = shift
				shift = 26
				shift = shift + remainder
			plain += alphaUpper[shift]
				
		if i in alphaLower:
			#Get plain text letter postion
			positionPlain = alphaLower.index(i)
		
			plainPositions.insert(k,positionPlain)
			k += 1
			shift = positionPlain - keyPositions[counter]
			
			
			if shift > 25:
				rem = shift - 26
				shift = rem
			if shift < 0:
				remainder = shift
				shift = 26
				shift = shift + remainder
			plain += alphaUpper[shift]	

			

		counter += 1
		

		if counter > 15:
			counter = 0
	return plain

#remove non alpha characters from string
message = removeChar(cipherText)
print "\nCiphertext"
print message
plainText = decrypt(message)

print "\nPlaintext"
print plainText

print "\nPassword"
print key
#print keyPositions
#print plainPositions

