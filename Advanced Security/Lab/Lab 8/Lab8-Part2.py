#!/usr/bin/python
from Crypto.PublicKey import RSA
from Crypto import Random

print "*************** Part 2 ***************"
print "RSA alogorithm"


src_data = 'jonathan riordan'
print `src_data`

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
print 'Key generated'

pub_key = key.publickey()
print 'Public key', pub_key

enc_data = pub_key.encrypt(src_data, 32)[0]
print `enc_data`

dec_data = key.decrypt(enc_data)
print `dec_data`