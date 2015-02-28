from .datatypes import *
from . import OrderedClass


class Structure(metaclass=OrderedClass):
    field_prefix = ''

    def __init__(self, stream, offset=0):
        self.stream = stream

        self.stream.seek(offset)

        for attrname in self.__class__.get_fields_names():
            print(attrname)
            setattr(self, attrname, getattr(
                self, attrname).parse(self.stream))

    @classmethod
    def get_fields_names(cls):
        return [attrname for attrname in cls.members
                if attrname.startswith(cls.field_prefix)]

    @classmethod
    def get_size(cls):
        return sum([getattr(cls, name).length
                    for name in cls.get_fields_names()])

    def __repr__(self):
        fields = "\n".join(
            ["\t{0} = {1}".format(attrname, getattr(self, attrname))
                for attrname in self.__class__.get_fields_names()])

        return "{0} \n {1}".format(self.__class__.__name__, fields)


class ELF_Header(Structure):
    field_prefix = 'e_'

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

    def get_section_header(self):
        return [SectionHeader(self.stream, self.e_shoff + (self.e_shentsize*i))
                for i in range(0, self.e_shnum-1)]

    def __init__(self, stream, offset=0):
        super(ELF_Header, self).__init__(stream, offset+16)


class SectionHeader(Structure):
    field_prefix = 'sh_'

    sh_name = ELF_Word
    sh_type = ELF_Word
    sh_flags = ELF_Xword
    sh_addr = ELF_Addr
    sh_offset = ELF_Off
    sh_size = ELF_Xword
    sh_link = ELF_Word
    sh_info = ELF_Word
    sh_addralign = ELF_Xword
    sh_entsize = ELF_Xword
