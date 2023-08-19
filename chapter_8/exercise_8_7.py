#Exercise 8.7 and 8.8
def make_album(artist, album, number_songs=None):
    album_info = {'artist': artist.title(), 'album': album.title()}

    if number_songs:
        album_info['number of songs'] = int(number_songs)
    
    return album_info

while True:
    artist = input("(Enter q to stop the program)\nEnter the name of the artist: ")
    
    if artist == 'q':
        break

    album = input("Enter the name of the album: ")
    number_songs = input("Enter the number of songs: ")

    print(make_album(artist, album, number_songs))