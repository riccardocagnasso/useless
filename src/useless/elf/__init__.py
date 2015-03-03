def parse_cstring(stream, offset):
    from .datatypes import ELF_Unsigned_Char
    stream.seek(offset)

    string = ""

    while True:
        char = ELF_Unsigned_Char.parse(stream)

        if char == b'\x00':
            return string
        else:
            string += char.decode()
