## COPYRIGHT STEVEN B. ROOSA  ALL RIGHTS RESERVED

import hashlib
import csv
import base64

def MD5(value):
    value_encoded = value.encode()
    hash_object = hashlib.md5(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def MD4(value):
    hash_object = hashlib.new('md4')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def RIPEMD160(value):
    hash_object = hashlib.new('ripemd160')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def WHIRLPOOL(value):
    hash_object = hashlib.new('whirlpool')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def SHA256(value):
    hash_object = hashlib.new('sha256')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def SHA1(value):
    hash_object = hashlib.new('sha1')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def SHA512(value):
    hash_object = hashlib.new('sha512')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def SHA224(value):
    hash_object = hashlib.new('sha224')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def SHA384(value):
    hash_object = hashlib.new('sha384')
    value_encoded = value.encode()
    hash_object.update(value_encoded)
    hash = (hash_object.hexdigest())
    return hash

def BASE64(value):
    b64_input = str.encode(value)
    B64 = base64.b64encode(b64_input)
    Encode = B64.decode()
    return Encode


OutputIDs = open('OutputIDs_txt', 'w')
OutputB64 = open('OutputB64_txt', 'w')

with open('IDs.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('IDs_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
    print(mydict)
    for key, val in mydict.items():

        print(key + "@\t<Unique_ID>", val + "--", key, file = OutputIDs)

        print((MD5(key)) + "@\t<Unique_ID>  MD5 of", val + "--", key, file = OutputIDs)  

        print((MD4(key)) + "@\t<Unique_ID>  MD4 of", val + "--", key, file = OutputIDs)

        print((RIPEMD160(key)) + "@\t<Unique_ID>  RIPEMD160 of", val + "--", key, file = OutputIDs)

        print((WHIRLPOOL(key)) + "@\t<Unique_ID>  WHIRLPOOL of", val + "--", key, file = OutputIDs)

        print((SHA256(key)) + "@\t<Unique_ID>  SHA256 of", val + "--", key, file = OutputIDs)

        print((SHA1(key)) + "@\t<Unique_ID>  SHA1 of", val + "--", key, file = OutputIDs)

        print((SHA512(key)) + "@\t<Unique_ID>  SHA512 of", val + "--", key, file = OutputIDs)

        print((SHA224(key)) + "@\t<Unique_ID>  SHA224 of", val + "--", key, file = OutputIDs)

        print((SHA384(key)) + "@\t<Unique_ID>  SHA384 of", val + "--", key, file = OutputIDs)

        print((BASE64(key)) + "@\t<Unique_ID>  BASE64 of", val + "--", key, file = OutputIDs)

## Meta Hashes

        hashlist = {MD5: 'MD5', MD4: 'MD4', RIPEMD160: 'RIPEMD160' , WHIRLPOOL: 'WHIRLPOOL', SHA256: 'SHA256', SHA1: 'SHA1', SHA512: 'SHA512', SHA224: 'SHA224', SHA384: 'SHA384', BASE64: 'BASE64' }

        for x, y in hashlist.items():

            print(((MD5(x(key)))) + "@\t<Unique_ID>  MD5 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((MD4(x(key)))) + "@\t<Unique_ID>  MD4 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((RIPEMD160(x(key)))) + "@\t<Unique_ID>  RIPEMD160 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((WHIRLPOOL(x(key)))) + "@\t<Unique_ID>  WHIRLPOOL of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((SHA256(x(key)))) + "@\t<Unique_ID>  SHA256 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((SHA1(x(key)))) + "@\t<Unique_ID>  SHA1 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((SHA512(x(key)))) + "@\t<Unique_ID>  SHA512 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((SHA224(x(key)))) + "@\t<Unique_ID>  SHA224 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((SHA384(x(key)))) + "@\t<Unique_ID>  SHA384 of " + y + " of", val + "--", key, file = OutputIDs)

        for x, y in hashlist.items():

            print(((BASE64(x(key)))) + "@\t<Unique_ID>  BASE64 of " + y + " of", val + "--", key, file = OutputIDs)

