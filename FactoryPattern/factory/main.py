from FactoryPattern.factory.model import Song
from FactoryPattern.factory.serializers import ObjectSerializer

if __name__ == '__main__':
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = ObjectSerializer()
    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))