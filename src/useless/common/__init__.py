import struct


def parse_cstring(stream, offset):
    """
        parse_cstring will parse a null-terminated string in a bytestream.

        The string will be decoded with UTF-8 decoder, of course since we are
        doing this byte-a-byte, it won't really work for all Unicode strings.

        TODO: add proper Unicode support
    """
    stream.seek(offset)

    string = ""

    while True:
        char = struct.unpack('c', stream.read(1))[0]

        if char == b'\x00':
            return string
        else:
            string += char.decode()
