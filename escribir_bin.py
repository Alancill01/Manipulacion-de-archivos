import struct
with open('test.bin', 'wb') as file:
    binary_data = struct.pack('3s i f', b'foo', 42, 3.14)
    file.write(binary_data)