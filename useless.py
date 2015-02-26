import struct
import collections


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

class ELF_Half(ELF_Sword):
    length = 2
    struct_type = 'H'

class ELF_Unsigned_Char(ELF_Sword):
    length = 1
    struct_type = 'c'

class ELF_Addr(ELFDataType):
    length = 4

    @classmethod
    def parse(cls, stream):
        return stream.read(cls.length)

class ELF_Off(ELF_Word):
    pass


class OrderedClass(type):

     @classmethod
     def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

     def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result


class ELF_Header(metaclass=OrderedClass):
    e_type = ELF_Half
    e_machine = ELF_Half
    e_version = ELF_Word
    e_entry = ELF_Addr
    e_phoff = ELF_Off
    e_shoff = ELF_Off
    e_flags = ELF_Word
    e_ehsize = ELF_Half
    e_phentsize = ELF_Half
    e_phnum = ELF_Half
    e_shentsize = ELF_Half
    e_shnum = ELF_Half
    e_shstrndx = ELF_Half

    def __init__(self, stream, offset=0):
        stream.seek(offset+16)

        for attrname in self.__class__.get_fields_names():
            setattr(self, attrname, getattr(
                self, attrname).parse(stream))

    @classmethod
    def get_fields_names(cls):
        return [attrname for attrname in cls.members
            if attrname.startswith('e_')]


    def __repr__(self):
        fields = "\n".join(["\t{0} = {1}".format(attrname, getattr(self, attrname))
            for attrname  in self.__class__.get_fields_names()])

        return "{0} \n {1}".format(self.__class__.__name__, fields)