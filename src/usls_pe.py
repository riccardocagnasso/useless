import argparse

from useless.PE import PE_File
from useless.display import *


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

    parser.add_argument('-d', '--dynsym',
                        dest='dynsym', action='store_true',
                        help='print content of dynamic symbol table')
    parser.set_defaults(dynsym=False)

    return parser.parse_args()


def main():
    args = get_argument_parser()

    stream = open(args.library, 'rb')

    PE = PE_File(stream)

    print(PE.coff_header)
    print(PE.optional_standard_fields)
    print(PE.optional_windows_fields)

    for dd in PE.optional_data_directories:
        print(dd)

    for se in PE.section_headers:
        print(se)

    print('EXPORT')
    print(PE.dir_export)

if __name__ == "__main__":
    main()
