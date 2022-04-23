# Io python
# 
# In this lesson you will learn about the IO functions of Python.
# This will enable you to read and write files as well as 
# read and write to serial devices such as the secure bootloader 
# you are designing during this course. A series of challenges
# follow which will require you to read Python documentation
# as well as other online resources. Good luck!### Challenge Name: echo_int (/embsec/io_python/echo_int)
# 
# 
#     1. Read a big-endian short from the serial device
#     2. Increment the integer by 1
#     3. Send the integer as a big-endian short back to the serial device
# 
# Resources:
# 
# <https://en.wikipedia.org/wiki/Endianness>
# 
# <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>
# 
# <https://docs.python.org/3/library/struct.html>
# 
# 
# 
from embsec import Serial
import struct

def echo_int():
    ser = Serial("/embsec/io_python/echo_int")
    x = ser.read(2) #reads/recieves evretyhing in the serial
    # Your code goes here!
    s = struct.unpack('>h', x) #actually unpacks the info in there, doesnt unpack the literal serail, as to recive/read and unpack info
    s = s[0] #start with the very first integer, read as list, tuple, to know what to incrment
    s += 1 #increments it
    y = struct.pack('>h', s) #repacks the info from s
    ser.write(y) #sends it back to serial
    print(ser.read_until()) #prints the lines until theres nothign


echo_int()

### Challenge Name: send_file (/embsec/io_python/send_file)
# 
# 
# 
#     1. Read 'file.bin' from your local system
#     2. Calculate the size
#     3. Send the size as a little-endian short
#     4. Send the file to serial device
# 
#     The serial device expects a little-endian short indicating the size of the
#     incoming data and then size bytes of data. The format is represented below:
#     
#     [ 0x02 ]  [ variable ]
#     ---------------------
#     | Length |  Data... |
#     ---------------------
# 
# Resources:
# 
# <https://en.wikipedia.org/wiki/Endianness>
# 
# <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>
# 
# <https://docs.python.org/3/library/struct.html>
# 
# <https://docs.python.org/3/tutorial/inputoutput.html>
# 
# 
from embsec import Serial
import struct
import os

def send_file():
    ser = Serial("/embsec/io_python/send_file")
    # Your code goes here!
    d = open('file.bin', 'rb') # opening the file and getting the bytes
    data = d.read() #reading the whole file, everything in it
    file_size = os.path.getsize('./file.bin') # gets the size of the file
    pack = struct.pack('<h', file_size) #packs the size as little endian short
    ser.write(pack) #sends it back to the serial
    f = struct.pack(f'<{file_size}s', data ) #packs everything/bytes within the content of the whoel fiel
    ser.write(f) # sends all of the content/bytes packs to the serial
    print(ser.read_until()) #reads until there is nothign
    

send_file()
### Challenge Name: send_large_file (/embsec/io_python/send_large_file)
# 
# 
#     1. Read 'large_file.bin' from your local system
#     3. Send the data in frames to the serial device (frame format below)
#     4. Send zero-length frame to indicate end of transmission
# 
#     The serial device expects that a frame begins with a little-endian short 
#     indicating the size of the frame and then frame data. The maximum frame 
#     size is 16 bytes. The frame format is represented below:
#     
#     [ 0x02 ]  [ up to 0xE bytes ]
#     ----------------------------
#     | Length |      Data...    |
#     ----------------------------
#     
# Resources:
# <https://en.wikipedia.org/wiki/Endianness>
# <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>
# <https://docs.python.org/3/library/struct.html>
# <https://docs.python.org/3/tutorial/inputoutput.html>
# <https://pyserial.readthedocs.io/en/latest/shortintro.html>
# 
# 
from embsec import Serial
import os
import struct

def send_large_file():
    ser = Serial("/embsec/io_python/send_large_file")
    d = open('large_file.bin', 'rb') #opens file in byte format
    content = d.read() #reads everything within it bytes
    file_size = os.path.getsize('./large_file.bin') #gets size of file
    
    number = int(file_size/14) #info in each frame, size per frame with max size of 14 since its short, 2 taken away
    last_number = file_size%14 #remaining in the last frame
    for i in range (number): #function for sending frames and content per full frame back to serial
        ser.write(struct.pack('<h', 14)) #sends full frames of data size in little endian short, in number, amuount per frame, so its getting data in 14 bytes mazx with data in full frame
        ser.write(content[14*i: 14*(i+1)]) #sends content of full frames, not size  per 14 byte max frame
    ser.write(struct.pack('<h', last_number)) #sends data size of last section thats not full frame
    ser.write(content[14*number:]) #sends content of data in last frame
    ser.write(struct.pack('<h', 0)) #sends 0 length 
    print(ser.read_until())
    # Your code goes here!
send_large_file()
