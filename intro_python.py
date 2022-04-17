
from embsec import Serial
ser = Serial('/embsec/intro_python/read_example')

def read_example():
    ser = Serial("/embsec/intro_python/read_example")
    # Your code goes here!
    d = ser.read()
    while d != b'\n':
        print(d.decode(), end='')
        d = ser.read()
read_example()


rom embsec import Serial
ser = Serial('/embsec/intro_python/write_example')

def write_example():
    ser = Serial("/embsec/intro_python/write_example")
    # Your code goes here!
    ser.write(b'hello world!\n')
    print(ser.read_until())

write_example()
