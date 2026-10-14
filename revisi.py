import os
from prettytable import PrettyTable

os.system("cls")

# watchlist (belum ditonton)
watchlist_judul = ["naruto", "black clover", "kny", "jjk", "horimiya"]
watchlist_genre = ["action", "action", "action", "action", "romance"]

# sudah ditonton
ditonton_judul = []
ditonton_genre = []


def tambah_anime():
    judul = input("Masukkan judul anime: ")
    if judul == "":
        print("Judul tidak boleh kosong.")
    elif judul in ditonton_judul:
        print("Anime sudah ditonton.")
    elif judul in watchlist_judul:
        print("Anime sudah ada di watchlist.")
    else:
        genre = input("Masukkan genre anime: ")
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
    daftar_watchlist()
    judul = input("Masukkan judul anime yang sudah ditonton: ")
    if judul in watchlist_judul:
        i = watchlist_judul.index(judul)
        ditonton_judul.append(watchlist_judul.pop(i))
        ditonton_genre.append(watchlist_genre.pop(i))
        print(judul, "dipindahkan ke daftar sudah ditonton.")
    else:
        print(judul, "tidak ada di watchlist.")


def daftar_ditonton():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Judul", "Genre"]
    for i in range(len(ditonton_judul)):
        tabel.add_row([i + 1, ditonton_judul[i], ditonton_genre[i]])
    print(tabel)


def hapus_anime():
    daftar_watchlist()
    judul = input("Masukkan judul anime yang ingin dihapus: ")
    if judul in watchlist_judul:
        i = watchlist_judul.index(judul)
        watchlist_judul.pop(i)
        watchlist_genre.pop(i)
        print(judul, "berhasil dihapus dari watchlist.")
    else:
        print(judul, "tidak ditemukan di watchlist.")


# ===== MENU UTAMA =====
while True:
    print("=== WATCHLIST ANIME ===")
    print("1. Tambah anime ke watchlist")
    print("2. Lihat watchlist")
    print("3. Tandai anime sudah ditonton")
    print("4. Lihat daftar anime yang sudah ditonton")
    print("5. Hapus anime dari watchlist")
    print("6. Keluar")
    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        tambah_anime()
    elif menu == "2":
        daftar_watchlist()
    elif menu == "3":
        tambah_ditonton()
    elif menu == "4":
        daftar_ditonton()
    elif menu == "5":
        hapus_anime()
    elif menu == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada, input lagi.")
