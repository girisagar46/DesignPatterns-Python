from FactoryPattern.factory.JsonSerializer import JsonSerializer
from FactoryPattern.factory.XmlSerializer import XmlSerializer
from FactoryPattern.factory.YamlSerializer import YamlSerializer


class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
factory.register_format('YAML', YamlSerializer)
