from cached_property import cached_property
from useless.elf.structures import *
from ..common import parse_cstring


ELF_HEADER_OFFSET_CONSTANT = 0x10


class ELF_File(object):
    """
        ELF_File represents a ELF dynamic object and provides methods to
        access all data structures
    """
    def __init__(self, stream):
        self.stream = stream

    @cached_property
    def header(self):
        return ELF_Header(self.stream, ELF_HEADER_OFFSET_CONSTANT)

    @property
    def sections(self):
        for i in range(0, self.header.e_shnum):
            yield ELF_SectionHeader(
                    self.stream,
                    self.header.e_shoff + (self.header.e_shentsize*i),
                    self)

    @cached_property
    def section_string_table(self):
        section_string_table_header = ELF_SectionHeader(
            self.stream, self.header.e_shoff +
            (self.header.e_shentsize*self.header.e_shstrndx), self)

        return ELF_StringTable(self.stream,
                               section_string_table_header.sh_offset)

    @cached_property
    def dynsym_string_table(self):
        dynstrheader = self.get_section_header_by_name('.dynstr')

        return ELF_StringTable(self.stream,
                               dynstrheader.sh_offset)

    @cached_property
    def symbol_table(self):
        for s in self.sections:
            if s.name == ".dynsym":
                i = 0
                symbol_size = ELF_Symbol.get_size()
                while (i+1)*symbol_size < s.sh_size:
                    i += 1
                    yield ELF_Symbol(self.stream,
                                     s.sh_offset + (i*symbol_size),
                                     self)

    def get_section_header_by_name(self, name):
        return list(filter(lambda s: s.name == name, self.sections))[0]
