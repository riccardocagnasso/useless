import struct


class ELFDataType(object):
    length = None
    struct_type = None

    @classmethod
    def parse(self, stream):
        return None


class ELF_Sword(ELFDataType):
    length = 4
    struct_type = 'I'

    @classmethod
    def parse(cls, stream):
        b = stream.read(cls.length)

        return struct.unpack(cls.struct_type, b)

class ELF_Word(ELF_Sword):
    struct_type = 'i'

class ELF_Half(ELF_Sword):
    length = 2
    struct_type = 'H'

class ELF_Unsigned_Char(ELF_Sword):
    length = 1
    struct_type = 'c'

class ELF_Off(ELFDataType):
    length = 4

    @classmethod
    def parse(cls, stream):
        return stream.read(cls.length)


class ELF_Header(object):