import struct


def parse_cstring(stream, offset):
    stream.seek(offset)

    string = ""

    while True:
        char = struct.unpack('c', stream.read(1))[0]

        if char == b'\x00':
            return string
        else:
            string += char.decode()
