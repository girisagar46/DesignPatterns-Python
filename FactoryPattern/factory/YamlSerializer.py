import yaml

from FactoryPattern.factory.JsonSerializer import JsonSerializer


class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)
