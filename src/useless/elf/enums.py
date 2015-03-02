from enum import IntEnum
from .datatypes import ELF_Word


class ELF_SectionType(IntEnum):
    SH_NULL = 0
    SHT_PROGBITS = 1
    SHT_SYMTAB = 2
    SHT_STRTAB = 3
    SHT_RELA = 4
    SHT_HASH = 5
    SHT_DYNAMIC = 6
    SHT_NOTE = 7
    SHT_NOBITS = 8
    SHT_REL = 9
    SHT_SHLIB = 10
    SHT_DYNSYM = 11

    @classmethod
    def parse(cls, stream):
        num = ELF_Word.parse(stream)

        try:
            return cls(num)
        except ValueError:
            return num
