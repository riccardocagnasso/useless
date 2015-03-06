class Magic(object):
    def __init__(self, stream):
        self.stream = stream

    def is_elf(self):
        self.stream.seek(0)
        return self.stream.read(4) == b'\x7fELF'

    def is_pe(self):
        self.stream.seek(0)
        magic = self.stream.read(2)
        is_dos = (magic == b'MZ') or (magic == b'ZM')

        return is_dos

        if not is_dos:
            return false
        else:
            try:
                PE = PE_File(stream)
                header = PE.header
            except Exception:
                return False

    def is_dynamic(self):
        pass
