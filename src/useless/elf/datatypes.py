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

        return struct.unpack(cls.struct_type, b)[0]


class ELF_Word(ELF_Sword):
    struct_type = 'i'


class ELF_Xword(ELF_Sword):
    length = 8
    struct_type = 'Q'


class ELF_Sxword(ELF_Sword):
    length = 8
    struct_type = 'q'


class ELF_Half(ELF_Sword):
    length = 2
    struct_type = 'H'


class ELF_Unsigned_Char(ELF_Sword):
    length = 1
    struct_type = 'c'


class ELF_Addr(ELFDataType):
    length = 8

    @classmethod
    def parse(cls, stream):
        return stream.read(cls.length)


class ELF_Off(ELF_Xword):
    pass
