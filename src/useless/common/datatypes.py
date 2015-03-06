import struct


class BinaryDataType(object):
    """
        Some datatype reppresented as an array of bytes.

        This will be automatically decoded in a structure.
    """

    length = None
    struct_type = None

    @classmethod
    def parse(cls, stream):        
        b = stream.read(cls.length)

        return struct.unpack(cls.struct_type, b)[0]
