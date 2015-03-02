import collections


class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result


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
