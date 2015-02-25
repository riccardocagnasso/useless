import struct


class ELFDataType(object):
    length = None
    struct_type = None

    @classmethod
    def parse(self, stream):
        return None


class ELF_Addr(ELFDataType):
    length = 4
    struct_type = 'I'

    @classmethod
    def parse(cls, stream):
        b = stream.read(cls.length)

        return struct.unpack(cls.struct_type, b)


class ELF_Half(ELF_Addr):
    length = 2
    struct_type = 'H'
