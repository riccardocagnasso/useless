import argparse
from useless.elf.structures import *
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
    header = ELF_Header(stream)

    if args.header:
        print(HeaderTable(header))

    if args.sections:
        print(SectionsTable(header.sections))

    if args.dynsym:
        print(SymbolsTable(header.symbol_table))

if __name__ == "__main__":
    main()
