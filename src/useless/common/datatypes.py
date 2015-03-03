import struct


class BinaryDataType(object):
    length = None
    struct_type = None

    @classmethod
    def parse(cls, stream):
        b = stream.read(cls.length)

        return struct.unpack(cls.struct_type, b)[0]
