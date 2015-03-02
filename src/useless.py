import argparse
from useless.elf.structures import *


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

    for s in header.sections:
        print(s.name)
        print(s)

if __name__ == "__main__":
    main()
