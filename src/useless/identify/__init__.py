class Magic(object):
    """
        This class basically serves to understand if the file is readable
        by useless and how to handle it.
    """
    def __init__(self, stream):
        self.stream = stream

    def is_elf(self):
        self.stream.seek(0)
        return self.stream.read(4) == b'\x7fELF'

    def is_pe(self):
        self.stream.seek(0)
        magic = self.stream.read(2)
        return is_dos = (magic == b'MZ') or (magic == b'ZM')
