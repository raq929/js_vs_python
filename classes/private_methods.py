class IPhone:
    play(self, songs):
        for song in songs:
            print(songs)


class Album:
    def __init__(self, songs=[], player):
        self.songs = songs
        self.player = player

    # This method is private. We could replace it with a completely different implementation and
    # the play() method would still work. The consumer of Album never has to worry about the implementation change
    # This is a convention in python, it's not enforced: the consumer is warned not to call it directly
    def _get_player(self):
        if self.player:
            return self.player
        return IPhone()

    def play(self):
        player = self._get_player()
        payer.play(self.songs)
