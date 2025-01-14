with open("./Data.txt", "r", encoding="utf-8") as file:
    lines = file.read().strip().split("\n")

songs_data = []
def pobranieDanychDoKolekcji():
    for i in range(0, len(lines), 6):
        song_dict = {
            "artist": lines[i].strip(),
            "album": lines[i+1].strip(),
            "songsNumber": int(lines[i+2].strip()),
            "year": int(lines[i+3].strip()),
            "downloadNumber": int(lines[i+4].strip())
        }
        songs_data.append(song_dict)
def wyswietlenieDanych():
    for song in songs_data:
        print(song["artist"])
        print(song["album"])
        print(song["songsNumber"])
        print(song["year"])
        print(song["downloadNumber"])
        print(" ")
pobranieDanychDoKolekcji()
wyswietlenieDanych()