
# One time pad
# 
# This lab covers an security flaw that arises in the one time pad when the same pad is used more than once. When 
# two messages are XORed with the same pad, you can XOR the ciphertexts together to get rid of the pad entirely. Use 
# this lab to explore how to XOR two strings, and then crack this poor implementation of the "Two time pad." ### Challenge Name: xor (/embsec/one_time_pad/xor)
# 
# 
# The XOR operation is very common in cryptography and security, since it is very useful and also very fast. It's used in
# many algorithms, including AES and the one time pad. Here, use the Python bitwise XOR to XOR two strings together.
#     
#     1. Read in two byte strings of length 16 from the serial device
#     2. Do a bitwise XOR on each character
#     3. Make a byte string out of the XORed result of each pair of characters
#     4. Send the byte string back over the serial
# 
# Resources:
# <https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html>
# 
# Additional resources (For the one-line solution. Do this AFTER completing it for the first time if you want an added challenge):
# <https://docs.python.org/3.3/library/functions.html#zip>
# 
# 
def xor():
    ser = Serial("/embsec/one_time_pad/xor")
    # Your code goes here!
    x = str(ser.read(16)) #reads 16 byte string of one group
    y = str(ser.read(16)) #reads 16 byte string of another group
    xxor = ord(x[0])
    lenx = len(x)
    for i in range(1,lenx):
   # Traverse string to find the XOR
        xxor = (xxor ^ (ord(x[i])))
        
    yxor = ord(y[0])
    leny = len(y)
    for i in range(1,leny):
   # Traverse string to find the XOR
        yxor = (yxor ^ (ord(y[i])))
        
    xarr = bytes(xxor)
    yarr = bytes(yxor)
    ser.write(xarr)
    ser.write(yarr)
    print(ser.read_until())

xor()

#sources:https://www.geeksforgeeks.org/program-to-find-the-xor-of-ascii-values-of-characters-in-a-string/ 
#https://www.educative.io/edpresso/how-to-convert-strings-to-bytes-in-python

# 
# The one time pad (OTP) is theoretically a perfectly secure encryption method that cannot be cracked. However,
# the main downside is that you must first exchange a pre-shared key that is the same size as the plaintext. Poor
# implementation of the OTP leads to severe vulnerabilities.
# 
# In this challenge, you will be given two ciphertexts which have been XORed using the same OTP. It is your job to
# extract the message from these ciphertexts given them and a list of possible plaintexts.
# 
#     1. Read in the two byte string ciphertexts of length 16
#     2. Read in the list of all possible plaintexts from "plaintexts.txt"
#     3. Perform your attack
#     4. Send back the two decoded ciphertexts (order does not matter)
# 
# Both of the plaintext strings will be contained within "plaintexts.txt"
# 
# The key to this attack is that when you XOR something with itself, it becomes zero. So for any number x, x ^ x is 0. 
# Here, you will be given two ciphertexts which look like A ^ K and B ^ K. If you XOR these together (A ^ K ^ B ^ K), 
# the key will cancel out, leaving you witl A ^ B. After this, cryptanalysis comes in to finish guessing the message. 
# However, in place of complex cryptanalysis, you have been given a list of possible plaintexts which you will use 
# to crack the one time pad. 
# 
# Resources:
# <https://en.wikipedia.org/wiki/One-time_pad>
# <https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html>
# <http://www.crypto-it.net/eng/attacks/two-time-pad.html>
# 
# 
ser = Serial("/embsec/one_time_pad/two_time_pad")
cipher_one = ser.read(16) #Reading in one string length 16 bytes
print(f"Ciphertext 1 is : {cipher_one}")
cipher_two = ser.read(16) #Reading in second string length of 16 bytes
print(f"Ciphertext 2 is : {cipher_two}")

A_to_B_list = []
for i in range (0,16):
    cipher_piece_one = cipher_one[i] #taking specific index
    cipher_piece_two = cipher_two[i] #taking specific index
    A_XOR_B = (cipher_piece_one ^ cipher_piece_two) #XOR-ing
    A_to_B_list.append(A_XOR_B) #Adding each XORed chunk to a list

A_to_B = bytearray(A_to_B_list) #turing the list into byte format 
print(A_to_B)

opened_text = open("plaintexts.txt" , "rb") #Opening and extracting data from plaintexts.txt
read_text = opened_text.read() 
compares = read_text.splitlines()

print(f"Length of the list is : {len(compares)}")


for x in range (0,1793):
    plaintext_1 = compares[x]
    A_list = []
    for i in range (0,16):
        A_to_b_1 = A_to_B[i] #taking specific index
        plain_piece= plaintext_1[i] #taking specific index
        A_list_piece = (A_to_b_1 ^ plain_piece) #XOR-ing
        A_list.append(A_list_piece) #Adding each XORed chunk to a list
        A_list_b = bytearray(A_list)
    for y in range (0,1793):
        plaintext_2 = compares[y] 
        if A_list_b == plaintext_2:
            print(f"Plaintext 1 is {plaintext_1}")
            print(f"Plaintext 2 is {plaintext_2}")
            break
        else:
            continue

#from embsec import Serial
#from cryptography.fernet import Fernet
#from Crypto.Cipher import AES
#from Crypto.Random import get_random_bytes
#from base64 import b64encode

#def two_time_pad():
 #   ser = Serial("/embsec/one_time_pad/two_time_pad")
  #  # Your code goes here!
   # one = str(ser.read(16))
    #two = str(ser.read(16))
    
    #key = Fernet.generate_key()
    #fernet = Fernet(key)
    #encOne = fernet.encrypt(one.encode())
    
    #key = Fernet.generate_key()
    #fernet = Fernet(key)
    #encTwo = fernet.encrypt(two.encode())
    
    
    #pl = open('plaintexts.txt') # opening the file 
    #plread = pl.readlines() #reading the whole file in list, everything in it
    
    #pl0 = str(plread[0])
    #plxor = ord(pl0[0])

    
    #lenpl = len(plread[0])
    
    #for i in range(1,lenpl):
      #  ixor = str(plread[i])
   # Traverse string to find the XOR
     #   plxor1 = (plxor ^ ord(ixor[i]))
    
    #pl1 = str(plread[1])
   # plxor1 = ord(pl1[1])
    
    #lenpl1 = len(plread[1])
    
    #for i in range(1,lenpl1):
      #  ixor1 = str(plread[i])
   # Traverse string to find the XOR
     #   plxor2 = (plxor ^ ord(ixor1[i]))
    
        
    #dec1 = bytes(plxor1)
    #dec2 = bytes(plxor2)
    
    #key = Fernet.generate_key()
    #fernet = Fernet(key)
    #decpl = fernet.decrypt(dec1).decode()
    
    #key = Fernet.generate_key()
    #fernet = Fernet(key)
    #decpl1 = fernet.decrypt(dec2).decode()
                               
    #ser.write(dec1)
    #ser.write(dec2)
   # print(ser.read_until())
    

        

                             
   

    #sources:https://stackoverflow.com/questions/50481366/bytes-to-string-in-aes-encryption-and-decryption-in-python-3
#https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

two_time_pad()



























