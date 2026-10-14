import os
from prettytable import PrettyTable

os.system("cls")

watchlist_judul = ["naruto", "black clover", "kny", "jjk", "horimiya"]
watchlist_genre = ["action", "action", "action", "action", "romance"]

ditonton_judul = []
ditonton_genre = []
ditonton_rating = []

def minta_rating(teks):
    while True:
        rating_input = input(teks)
        if not rating_input.isdigit():
            print("Rating harus berupa angka.")
        else:
            rating = int(rating_input)
            if rating < 0 or rating > 10:
                print("Rating harus antara 0 - 10.")
            else:
                return rating

def tambah_anime():
    while True:
        print("Ketik 'selesai' kalau sudah tidak ingin memasukkan watchlist lagi.")
        judul = input("Masukkan judul anime: ")
        if judul == "selesai":
            break
        elif judul == "":
            print("Judul tidak boleh kosong.")
        elif judul in ditonton_judul:
            print("Anime sudah ditonton.")
        elif judul in watchlist_judul:
            print("Anime sudah ada di watchlist.")
        else:
            genre = input("Masukkan genre anime: ")
            if genre == "":
                print("Genre tidak boleh kosong.")
            else:
                watchlist_judul.append(judul)
                watchlist_genre.append(genre)
                print("Anime ditambahkan ke watchlist.")

def daftar_watchlist():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Judul", "Genre"]
    for i in range(len(watchlist_judul)):
        tabel.add_row([i + 1, watchlist_judul[i], watchlist_genre[i]])
    print(tabel)

def tambah_ditonton():
    while True:
        print("Daftar watchlist:")
        daftar_watchlist()
        print("Ketik 'selesai' kalau sudah selesai.")
        judul = input("Masukkan judul anime yang sudah ditonton: ")
        if judul == "selesai":
            break
        elif judul in watchlist_judul:
            rating = minta_rating("Masukkan rating (0-10): ")
            i = watchlist_judul.index(judul)
            ditonton_judul.append(watchlist_judul.pop(i))
            ditonton_genre.append(watchlist_genre.pop(i))
            ditonton_rating.append(rating)
            print(judul, "dipindahkan ke daftar sudah ditonton dengan rating", rating)
        else:
            print(judul, "tidak ada di watchlist.")

def daftar_ditonton():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Judul", "Genre", "Rating"]
    for i in range(len(ditonton_judul)):
        tabel.add_row([i + 1, ditonton_judul[i], ditonton_genre[i], ditonton_rating[i]])
    print(tabel)

def ubah_ditonton():
    if len(ditonton_judul) == 0:
        print("Belum ada anime yang selesai ditonton.")
        return
    while True:
        print("Daftar anime yang sudah ditonton:")
        daftar_ditonton()
        print("Ketik 'selesai' kalau sudah selesai.")
        judul = input("Masukkan judul anime yang ingin diubah ratingnya: ")
        if judul == "selesai":
            break
        elif judul in ditonton_judul:
            rating = minta_rating("Masukkan rating baru untuk " + judul + " (0-10): ")
            ditonton_rating[ditonton_judul.index(judul)] = rating
            print("Rating", judul, "berhasil diubah menjadi", rating)
        else:
            print(judul, "tidak ada di daftar yang sudah ditonton.")

def hapus_anime():
    while True:
        print("Daftar watchlist:")
        daftar_watchlist()
        print("Ketik 'selesai' kalau sudah selesai.")
        judul = input("Masukkan judul anime yang ingin dihapus dari watchlist: ")
        if judul == "selesai":
            break
        elif judul in watchlist_judul:
            i = watchlist_judul.index(judul)
            watchlist_judul.pop(i)
            watchlist_genre.pop(i)
            print(judul, "berhasil dihapus dari watchlist.")
        else:
            print(judul, "tidak ditemukan di watchlist.")

while True:
    print("=== WATCHLIST ANIME ===")
    print("1. Tambah anime ke watchlist")
    print("2. Lihat watchlist")
    print("3. Tandai anime sudah ditonton + beri rating")
    print("4. Lihat daftar anime yang sudah ditonton")
    print("5. Ubah rating anime yang sudah ditonton")
    print("6. Hapus anime dari watchlist")
    print("7. Keluar")
    menu = input("Pilih menu (1-7): ")

    if menu == "1":
        tambah_anime()
    elif menu == "2":
        daftar_watchlist()
    elif menu == "3":
        tambah_ditonton()
    elif menu == "4":
        daftar_ditonton()
    elif menu == "5":
        ubah_ditonton()
    elif menu == "6":
        hapus_anime()
    elif menu == "7":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada, input lagi.")