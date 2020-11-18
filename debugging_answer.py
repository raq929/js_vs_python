class Album:
    def __init__(self, songs=[]):
        self.songs = songs
        self.player = player

    def track_order(self, song):
        if song in self.songs:
            return self.songs.index(song)
        raise Error(f'{song} is not in this album')

    def set_song_order(self, song, new_index):
        current_index = self.track_order(song)
        insert_index = new_index
        if current_index < new_index:
            insert_index = new_index - 1
        self.songs.remove(song)
        self.songs.insert(insert_index, song)
