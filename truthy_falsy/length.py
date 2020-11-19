class Album:
    def __init__(self, songs=[]):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __bool__(self):
        return len(self.songs) > 0


class AlbumWithoutLenAndBool:
    def __init__(self, songs=[]):
        self.songs = songs


def print_if_true(album):
    if album:
        print("Album was truthy!")
    else:
        print("Album was falsey!")