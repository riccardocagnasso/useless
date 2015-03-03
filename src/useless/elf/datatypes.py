import struct
from ..common.datatypes import BinaryDataType


class ELF_Sword(BinaryDataType):
    length = 4
    struct_type = 'I'


class ELF_Word(ELF_Sword):
    struct_type = 'i'


class ELF_Xword(BinaryDataType):
    length = 8
    struct_type = 'Q'


class ELF_Sxword(BinaryDataType):
    length = 8
    struct_type = 'q'


class ELF_Half(BinaryDataType):
    length = 2
    struct_type = 'H'


class ELF_Unsigned_Char(BinaryDataType):
    length = 1
    struct_type = 'c'


class ELF_Addr(BinaryDataType):
    length = 8
    struct_type = 'Q'

    @classmethod
    def parse(self, stream):
        return hex(super(ELF_Addr, self).parse(stream))


class ELF_Off(ELF_Xword):
    pass
