class Album:
    def __init__(self, songs=[]):
        self.songs = songs
        self.player = player

    def track_order(self, song):
        if song in self.songs:
            return self.songs.index(song)
        raise Error(f'{song} is not in this album')

    def set_song_order(self, song, new_index):
        self.songs.remove(song)
        import pdb; pdb.set_trace()
        self.songs.insert(new_index, song)


lemonade = Album(songs=['Pray you catch me', 'Hold up', 'Sorry', 'Love Drought', 'Freedom', 'Formation'])