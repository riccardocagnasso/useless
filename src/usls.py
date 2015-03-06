import argparse
from useless.elf import ELF_File
from useless.PE import PE_File
from useless.identify import Magic
import useless.display.elf as elf_display
import useless.display.PE as PE_display


def get_argument_parser():
    parser = argparse.ArgumentParser(
        prog='useless',
        description='Useless is useless. Oh yeah, and parses bit and pieces' +
        'of ELF and PE dynamic libraries')

    parser.add_argument('library', type=str,
                        help='library to parse')

    parser.add_argument('-H', '--header',
                        dest='header', action='store_true',
                        help='print the Header')
    parser.set_defaults(header=False)

    parser.add_argument('-s', '--sections',
                        dest='sections', action='store_true',
                        help='print sections list')
    parser.set_defaults(sections=False)

    parser.add_argument('-S', '--symbols',
                        dest='symbols', action='store_true',
                        help='print content of dynamic symbol table')
    parser.set_defaults(dynsym=False)

    return parser.parse_args()


def main():
    args = get_argument_parser()

    stream = open(args.library, 'rb')

    magic = Magic(stream)

    if magic.is_elf():
        ELF = ELF_File(stream)

        if args.header:
            print('Header')
            print(elf_display.HeaderTable(ELF.header))

        if args.sections:
            print('Sections')
            print(elf_display.SectionsTable(ELF.sections))

        if args.symbols:
            print("Symbols")
            print(elf_display.SymbolsTable(ELF.symbol_table))
    elif magic.is_pe():
        PE = PE_File(stream)

        if args.header:
            print('Headers')
            print(PE_display.Header(PE.coff_header,
                                    PE.optional_standard_fields,
                                    PE.optional_windows_fields))

        if args.sections:
            print('Sections')
            print(PE_display.Sections(PE.section_headers))
            print('Directories')
            print(PE_display.Directories(PE.optional_data_directories))

        if args.symbols:
            print('Exported Symbols')
            print(PE_display.ExportTable(PE.dir_export_table))

            print('Imported Symbols')
            print(PE_display.ImportTable(PE.dir_import_table))
    else:
        print("library is not a ELF nor a PE/COFF file")


if __name__ == "__main__":
    main()
