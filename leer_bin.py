import struct
with open('test.bin', 'rb') as file:
    binary_data = file.read()
if len(binary_data) == 12:
    unpacked_data = struct.unpack('3s i f', binary_data)
    print("Datos desempaquetados:", unpacked_data)
else:
    print(f"Error: se esperaban 12 bytes, pero se obtuvieron {len(binary_data)} bytes.")