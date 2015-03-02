import argparse
from useless.elf.structures import *
import pprint


def get_argument_parser():
    parser = argparse.ArgumentParser(
        prog='useless',
        description='Useless is useless. Oh yeah, and parses bit and pieces' +
        'of ELF and PE dynamic libraries')

    parser.add_argument('library', type=str,
                        help='library to parse')

    return parser.parse_args()


def main():
    args = get_argument_parser()

    print(args.library)

    stream = open(args.library, 'rb')

    header = ELF_Header(stream)

    pp = pprint.PrettyPrinter(indent=4)

    for s in header.sections:
        pp.pprint(s.name)
        pp.pprint(s)

    for s in header.symbol_table:
        pp.pprint(s.name)
        pp.pprint(s)

if __name__ == "__main__":
    main()
