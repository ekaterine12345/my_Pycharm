class Song:
    def __init__(self, title, album, singer, deletion):
        self.title = title
        self.album = album
        self.singer = singer
        self.deletion = deletion

    def __str__(self):
        return f"title: {self.title}, album: {self.album}, singer: {self.singer}, deletion: {self.deletion}"


class Playlist:
    def __init__(self, album, songs=[]):
        self.album = album
        self.songs = songs

    def __str__(self):
        str1 = f"album: {self.album}, songs: ["
        for each in self.songs:
            str1 += f"{each},"
            str1 += ' '
        str1 += ']'
        return str1
    #
    # def pri(self):
    #     str1 = f"album: {self.album}, songs: ["
    #     for each in self.songs:
    #         print("str", each)
    #     return 0

    def add_song(self, song):
        print(song)
        self.songs.append(song)

    def __add__(self, other):
        return Playlist('merged_playlist', self.songs+other.songs)


song1 = Song('t1', 'a1', 'si1', 'del1')
song2 = Song('t2', 'a2', 'si2', 'del2')

playlist1 = Playlist('a1', [song1])
print(song1)
print(playlist1)
playlist1.add_song(song2)
print(playlist1)

print('########################')

song3 = Song('t3', 'a3', 'si3', 'del3')
song4 = Song('t4', 'a4', 'si4', 'del4')

playlist2 = Playlist('a3', [song3])
print(song3)
print(playlist2)
playlist2.add_song(song4)
print(playlist2)


print('##########################################')
playlist3 = playlist1+playlist2
print(playlist3)

