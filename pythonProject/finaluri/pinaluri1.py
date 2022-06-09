class Song:
    def __init__(self, title, singer, deletion, album=[]):
        self.title = title
        self.album = album
        self.singer = singer
        self.deletion = deletion

    def __str__(self):
        return f"title: {self.title}, album: {self.album}, singer: {self.singer}, deletion: {self.deletion}"


class Playlist:
    def __init__(self, album, max_songs, songs=[]):
        self.album = album
        self.songs = songs
        self.max_songs = max_songs

    def __str__(self):
        return f"album: {self.album}, max_songs {self.max_songs}, songs {self.songs} "

    def add_song(self, other):
        print(other)
        if self.max_songs > len(self.songs):
            self.songs.append(other)
            print(type(other), other.album)
            other.album.append(self)

    def __add__(self, other):
        return Playlist('joined_playlist.', self.songs + other.songs)


song1 = Song('t1',  'si1', 'del1', ['a1', 'a15'])
song2 = Song('t2',  'si2', 'del2', ['a2', 'a50'])
print(song1)
print(song2)

playlist1 = Playlist('a1', 15,  [song1])
print(playlist1)

playlist1.add_song(song2)
print(playlist1)
print(song2)

print('########################')

song3 = Song('t3',  'si3', 'del3', ['a3', 'a5'])
song4 = Song('t4',  'si4', 'del4',  ['a4', 'a54'])

playlist2 = Playlist('a3', 12, [song3])
print(song3)
print(playlist2)
playlist2.add_song(song4)
print(playlist2)


print('##########################################')
playlist3 = playlist1+playlist2
print(playlist3)

