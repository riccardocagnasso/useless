import struct
from ..common.datatypes import BinaryDataType


class PE_Char(BinaryDataType):
    length = 1
    struct_type = 'B'


class PE_Word(BinaryDataType):
    length = 2
    struct_type = 'H'


class PE_DWord(BinaryDataType):
    length = 4
    struct_type = 'I'


class PE_NameField(BinaryDataType):
    length = 8
    struct_type = 'c'

    @classmethod
    def parse(cls, stream):
        string = ""

        for i in range(0, cls.length):
            char = struct.unpack('c', stream.read(1))[0]

            if char == b'\x00':
                pass
            else:
                string += char.decode()

        return string

"""class PE_Addr(PE_Word):
    @classmethod
    def parse(cls, stream):
        return hex(super(PE_Addr, self).parse(stream))


class PE_DAddr(PE_DWord):
    @classmethod
    def parse(cls, stream):
        return hex(super(PE_Addr, self).parse(stream))"""
