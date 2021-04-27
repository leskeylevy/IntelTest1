"Triple DES is the successor to the original Data Encryption Standard (DES) algorithm, created in response to hackers who figured out how to breach DES. It’s a symmetric encryption that was once the most widely used symmetric algorithm in the industry, though it’s being gradually phased out. TripleDES applies the DES algorithm three times to every data block and is commonly used to encrypt UNIX passwords and ATM PINs."


from Crypto.Cipher import DES3

key = [
     1,  2,  3,  4,  5,  6,  7,  8, 
     9, 10, 11, 12, 13, 14, 15, 16, 
     17, 18, 19, 20, 21, 22, 23, 24
]

iv = [65, 110, 68, 26, 69, 178, 200, 219]

keyStr = ""
ivStr = ""

for i in key: 
    keyStr += chr(i)

for i in iv: 
    ivStr += chr(i)

encr = DES3.new(keyStr, DES3.MODE_CBC, ivStr)
decr = DES3.new(keyStr, DES3.MODE_CBC, ivStr)

#Outputs "1234567891234567"
print decr.decrypt(encr.encrypt("1234567891234567"))