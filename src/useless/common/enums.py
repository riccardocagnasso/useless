from enum import IntEnum


class BinaryEnum(IntEnum):
    """
        A Enum that is reppresented as an array of bytes.
        This class exists only to enable automatic parse via introspection
        in Structure
    """
    pass
