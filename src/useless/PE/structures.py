from .datatypes import *
from ..common.structures import *
from cached_property import cached_property


class COFF_Header(Structure):
    Magic = PE_DWord
    Machine = PE_Word
    NumberOfSections = PE_Word
    TimeDateStamp = PE_DWord
    PointerToSymbolTable = PE_DWord
    NumberOfSymbols = PE_DWord
    SizeOfOptionalHeader = PE_Word
    Characteristics = PE_Word


class OptionalHeader_StandardFields(Structure):
    Magic = PE_Word
    MajorLinkerVersion = PE_Char
    MinorLinkerVersion = PE_Char
    SizeOfCode = PE_DWord
    SizeOfInitializedData = PE_DWord
    SizeOfUninitializedData = PE_DWord
    AddressOfEntryPoint = PE_DWord
    BaseOfCode = PE_DWord
    BaseOfData = PE_DWord


class OptionalHeader_WindowsFields(Structure):
    ImageBase = PE_DWord
    SectionAlignment = PE_DWord
    FileAlignment = PE_DWord
    MajorOperatingSystemVersion = PE_Word
    MinorOperatingSystemVersion = PE_Word
    MajorImageVersion = PE_Word
    MinorImageVersion = PE_Word
    MajorSubsystemVersion = PE_Word
    MinorSubsystemVersion = PE_Word
    Win32VersionValue = PE_DWord
    SizeOfImage = PE_DWord
    SizeOfHeaders = PE_DWord
    CheckSum = PE_DWord
    Subsystem = PE_Word
    DllCharacteristics = PE_Word
    SizeOfStackReserve = PE_DWord
    SizeOfStackCommit = PE_DWord
    SizeOfHeapReserve = PE_DWord
    SizeOfHeapCommit = PE_DWord
    LoaderFlags = PE_DWord
    NumberOfRvaAndSizes = PE_DWord


class OptionalHeader_DataDirectory(Structure):
    VirtualAddress = PE_DWord
    Size = PE_DWord


class Section_Header(Structure):
    Name = PE_NameField
    VirtualSize = PE_DWord
    VirtualAddress = PE_DWord
    SizeOfRawData = PE_DWord
    PointerToRawData = PE_DWord
    PointerToRelocations = PE_DWord
    PointerToLinenumbers = PE_DWord
    NumberOfRelocations = PE_Word
    NumberOfLinenumbers = PE_Word
    Characteristics = PE_DWord


class Import_DirectoryTable(Structure):
    ImportLookupTableRVA = PE_DWord
    TimeDateStamp = PE_DWord
    ForwarderChain = PE_DWord
    NameRVA = PE_DWord
    ImportAddressTableRVA = PE_DWord

    def is_empty(self):
        return not any([getattr(self, x) == 0
                        for x in self.get_fields_names()])


class Export_DirectoryTable(Structure):
    ExportFlags = PE_DWord
    TimeDateStamp = PE_DWord
    MajorVersion = PE_Word
    MinorVersion = PE_Word
    NameRVA = PE_DWord
    OrdinalBase = PE_DWord
    AddressTableEntries = PE_DWord
    NumberOfNamePointers = PE_DWord
    ExportAddressTableRVA = PE_DWord
    NamePointerRVA = PE_DWord
    OrdinalTableRVA = PE_DWord

    def __init__(self, stream, offset, pe):
        self.pe = pe
        super(Export_DirectoryTable, self).__init__(stream, offset)

    @cached_property
    def Name(self):
        return parse_cstring(self.stream, self.pe.resove_rva(self.NameRVA))
