from cached_property import cached_property
from useless.PE.structures import *
from useless.PE.datatypes import *
from ..common import parse_cstring

PE_HEADER_OFFSET_CONSTANT = 0x3c


class PE_File(object):
    def __init__(self, stream):
        self.stream = stream

        self.stream.seek(PE_HEADER_OFFSET_CONSTANT)
        self.pe_header_offset = PE_Word.parse(stream)

    @cached_property
    def coff_header(self):
        return COFF_Header(self.stream, self.pe_header_offset)

    @cached_property
    def optional_standard_fields(self):
        return OptionalHeader_StandardFields(
            self.stream,
            self.pe_header_offset + COFF_Header.get_size())

    @cached_property
    def optional_windows_fields(self):
        offset = self.pe_header_offset +\
            COFF_Header.get_size() +\
            OptionalHeader_StandardFields.get_size()
        return OptionalHeader_WindowsFields(self.stream, offset)

    @property
    def optional_data_directories(self):
        base_offset = self.pe_header_offset +\
            COFF_Header.get_size() +\
            OptionalHeader_StandardFields.get_size() +\
            OptionalHeader_WindowsFields.get_size()

        for i in range(0, self.optional_windows_fields.NumberOfRvaAndSizes):
            offset = base_offset + i*OptionalHeader_DataDirectory.get_size()
            header = OptionalHeader_DataDirectory(self.stream, offset, i)

            if not header.is_empty():
                yield header

    @property
    def section_headers(self):
        base_offset = self.pe_header_offset +\
            COFF_Header.get_size() +\
            OptionalHeader_StandardFields.get_size() +\
            OptionalHeader_WindowsFields.get_size() +\
            OptionalHeader_DataDirectory.get_size() * \
            self.optional_windows_fields.NumberOfRvaAndSizes

        for i in range(0, self.coff_header.NumberOfSections):
            offset = base_offset + i*Section_Header.get_size()
            yield Section_Header(self.stream, offset)

    def get_section_of_rva(self, rva):
        for s in self.section_headers:
            if s.VirtualAddress <= rva and\
               (s.VirtualAddress + s.VirtualSize) > rva:
                return s

    def resolve_rva(self, rva):
        containing_section = self.get_section_of_rva(rva)

        in_section_offset = containing_section.PointerToRawData -\
            containing_section.VirtualAddress

        return in_section_offset + rva

    @cached_property
    def dir_export_table(self):
        export_header = list(self.optional_data_directories)[0]
        export_offset = self.resolve_rva(export_header.VirtualAddress)

        return Export_DirectoryTable(self.stream, export_offset, self)

    @property
    def dir_import_table(self):
        import_header = list(self.optional_data_directories)[1]
        import_offset = self.resolve_rva(import_header.VirtualAddress)

        i = 0
        while True:
            offset = import_offset + i*Import_DirectoryTable.get_size()
            idt = Import_DirectoryTable(self.stream, offset, self)

            if idt.is_empty():
                break
            else:
                yield idt

            i += 1
