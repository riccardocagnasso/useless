from .datatypes import *
from ..common.structures import *


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
