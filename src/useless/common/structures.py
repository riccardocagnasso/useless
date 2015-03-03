import collections


class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result


class Structure(metaclass=OrderedClass):
    field_prefix = ''

    def __init__(self, stream, offset=0):
        self.stream = stream

        self.stream.seek(offset)

        for attrname in self.__class__.get_fields_names():
            setattr(self, attrname, getattr(
                self, attrname).parse(self.stream))

    @classmethod
    def get_fields_names(cls):
        return [attrname for attrname in cls.members
                if attrname.startswith(cls.field_prefix)]

    @classmethod
    def get_size(cls):
        return sum([getattr(cls, name).length
                    for name in cls.get_fields_names()])

    def __repr__(self):
        fields = "\n".join(
            ["\t{0} = {1}".format(attrname, getattr(self, attrname).__repr__())
                for attrname in self.__class__.get_fields_names()])

        return "{0} \n {1}".format(self.__class__.__name__, fields)
