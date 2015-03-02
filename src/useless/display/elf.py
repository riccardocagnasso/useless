from prettytable import PrettyTable


class HeaderTable(PrettyTable):
    def __init__(self, elf_header):
        super(HeaderTable, self).__init__([
            'Type',
            'Machine',
            'Entry Point',
            'Program Header',
            'Section Header',
            "Flags"
        ])

        self.add_row(elf_header)

    def add_row(self, h):
        super(HeaderTable, self).add_row([
            h.e_type,
            h.e_machine,
            h.e_entry,
            "offset: {0} entry size: {1} entries: {2}".format(
                h.e_phoff, h.e_phentsize, h.e_phnum),
            "offset: {0} entry size: {1} entries: {2} strtab offset {3}"
            .format(h.e_shoff, h.e_shentsize, h.e_shnum, h.e_shstrndx),
            h.e_flags
        ])


class SectionsTable(PrettyTable):
    def __init__(self, sections):
        super(SectionsTable, self).__init__([
            'Name',
            'Type',
            'Flags',
            'Address',
            'Size',
            "Address Aligment",
            "Link"
        ])

        for s in sections:
            self.add_row(s)

    def add_row(self, s):
        super(SectionsTable, self).add_row([
            "offset: {0} value: {1}".format(s.sh_name, s.name),
            s.sh_type.__repr__(),
            s.sh_flags,
            "address: {0} offset {1}".format(s.sh_addr, s.sh_offset),
            "size: {0} entry size {1}".format(s.sh_size, s.sh_entsize),
            s.sh_addralign,
            s.sh_link
        ])


class SymbolsTable(PrettyTable):
    def __init__(self, symbols):
        super(SymbolsTable, self).__init__([
            "Name",
            "Info",
            "Other",
            "Section Table Index",
            "Value",
            "Size"
        ])

        for s in symbols:
            self.add_row(s)

    def add_row(self, s):
        super(SymbolsTable, self).add_row([
            "offset: {0} value {1}".format(s.st_name, s.name),
            s.st_info,
            s.st_other,
            s.st_shndx,
            s.st_value,
            s.st_size
        ])
