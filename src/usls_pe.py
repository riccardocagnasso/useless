import argparse

from useless.PE import PE_File
from useless.display.PE import *


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

    PE = PE_File(stream)

    if args.header:
        print('Headers')
        print(Header(PE.coff_header,
                     PE.optional_standard_fields, PE.optional_windows_fields))

    if args.sections:
        print('Sections')
        print(Sections(PE.section_headers))
        print('Directories')
        print(Directories(PE.optional_data_directories))

    if args.symbols:
        print('Exported Symbols')
        print(ExportTable(PE.dir_export_table))

        print('Imported Symbols')
        print(ImportTable(PE.dir_import_table))

if __name__ == "__main__":
    main()
