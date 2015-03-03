from cached_property import cached_property
from useless.PE.structures import *
from useless.PE.datatypes import *

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
            yield OptionalHeader_DataDirectory(self.stream, offset)

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
        sections = sorted(self.section_headers, key=lambda s: s.VirtualAddress)

        prev = None
        for s in sections:
            if s.VirtualAddress > rva:
                return prev
            else:
                prev = s

    @cached_property
    def dir_export(self):
        export_header = list(self.optional_data_directories)[0]
        containing_section = self.get_section_of_rva(
            export_header.VirtualAddress)

        return containing_section
