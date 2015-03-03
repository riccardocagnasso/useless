import struct


class BinaryDataType(object):
    length = None
    struct_type = None

    @classmethod
    def parse(cls, stream):
        b = stream.read(cls.length)

        return struct.unpack(cls.struct_type, b)[0]


class PE_Word(BinaryDataType):
    length = 2
    struct_type = 'H'


class PE_DWord(BinaryDataType):
    length = 2
    struct_type = 'I'


"""class PE_Addr(PE_Word):
    @classmethod
    def parse(cls, stream):
        return hex(super(PE_Addr, self).parse(stream))


class PE_DAddr(PE_DWord):
    @classmethod
    def parse(cls, stream):
        return hex(super(PE_Addr, self).parse(stream))"""
