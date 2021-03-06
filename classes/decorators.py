class Album:
    all_albums = []

    def __init__(self, name, songs=[]):
        self.songs = songs
        self.name = name
        self.all_albums.append(self)

    # This decorator makes this method available to the class itself, not instances of the class
    @classmethod
    def all(cls):
        return cls.all_albums


    def __repr__(self):
        return f'{type(self)}: {self.name}'


Album('Lemonade')
Album('Dirty Computer')
print(Album.all())