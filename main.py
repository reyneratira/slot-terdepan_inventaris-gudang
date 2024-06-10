users = {
    "admin": "123",
}

barang = [
    {"Nama": "Kursi", "kode": "1"},
    {"Nama": "Meja",  "kode": "2"},
    {"Nama": "Sofa",  "kode": "3"},
    {"Nama": "Kasur", "kode": "4"},
    {"Nama": "Lampu", "kode": "5"},
] 

def landing():
    print("====== Selamat Datang Di Aplikasi Inventaris Gudang!! =====")
    print("")
    while True:
        print("Anda Ingin Masuk Sebagai : ")
        print("1. Admin")
        print("2. User")
        print("")

        try :
            pilihan = int(input("Masukkan Pilihan Anda: "))
            print("")
            if pilihan == 1:
                login()
                break
            elif pilihan == 2:
                menu_user()
                break
            else:
                print("Silahkan Pilih Sesuai Yang Tertera")
                print("")
        except(ValueError):
            print("Masukan Angka Sesuai Pilihan yang tertera")
            print("")
        
    

def check_user_password(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

def login():
    print("=====Welcome to the login system!=====")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("")

    attemp = 0
    while attemp < 2:
        if check_user_password(username, password):
            print("Login successful!")
            print("Welcome Admin!!")
            print("")
            menu_admin()
            break
        else:
            print("Invalid username or password. Please try again.")
            attemp += 1
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print("")
    else:
        print("Anda telah melampaui jumlah percobaan maksimum. Sistem sekarang akan ditutup!!")
        exit()

def menu_admin():
    while True :
        print("")
        print("========== MENU ADMIN ==========")
        try:
            print("1. Lihat Barang")
            print("2. Tambah Barang")
            print("3. Edit Nama Barang Barang")
            print("4. Cari Barang Menurut Kode")
            print("5. Hapus Barang")
            print("6. Keluar")
            pil_menu = int(input("Masukan Angka Pilihan Yang Tertera : "))
            print("")

            if pil_menu == 1 :
                lihatmenuAd(barang)
            elif pil_menu == 2 :
                tambahmenuAd(barang)
            elif pil_menu == 3 :
                editmenuAd(barang)
            elif pil_menu == 4 :
                carimenuAd(barang)
            elif pil_menu == 5 :
                hapusmenuAd(barang)
            elif pil_menu == 6 : 
                keluarAd()
            else:
                print("Pilihan Invalid, Mohon Input Ulang")
                print("")
                menu_admin()
        except(ValueError):
            print("Mohon masukan angka")
def menu_user():
    while True:
        print("")
        try :
            print("========== MENU USER ==========")
            print("1. Lihat Barang")
            print("2. Cari Barang")
            print("3. Keluar") 
            pil_menus = int(input("Masukan Angka Pilihan Yang Tertera : "))
            print("")

            if pil_menus == 1:
                lihatmenuUs(barang)
            elif pil_menus == 2:
                carimenuUs(barang)
            elif pil_menus == 3:
                keluarUs()
            else:
                print("Pilihan Invalid, Mohon Input Ulang")
                menu_user()
        except(ValueError):
            print("Mohon masukan angka")

def tambahmenuAd(barang):
    try:
        jumlah = int(input("Berapa Barang yang ingin ditambahkan (Angka): "))
        print("")
        while jumlah > 0:
            kode_barang = input("Masukkan kode barang: ")
            nama = input("Masukkan Nama barang: ")
            barang.append({"Nama": nama, "kode": kode_barang})
            jumlah -= 1
        print(f"Berhasil menambahkan barang ke daftar barang.")
        print("")
        menu_admin()
    except(ValueError):
        print("Mohon masukan input yang sesuai")

def lihatmenuAd(barang):
    print("========== Data Barang ==========")
    if not barang:
        print("Tidak ada barang dalam daftar.")
    else:
        for idx, item in enumerate(barang, start=1):
            print(f"{idx}. Nama: {item['Nama']}, Kode: {item['kode']}")
    print("")
    menu_admin()

def carimenuAd(barang):
    search_value = input("Masukkan kode barang yang ingin Anda cari: ")
    print("")
    found = False
    for item in barang:
        if item['Nama'] == search_value or item['kode'] == search_value:
            print(f"Barang dengan kode '{search_value}' memunculkan barang '{item['Nama']}'")
            print("")
            found = True
            break
    if not found:
        print(f"Barang dengan kode '{search_value}' tidak ditemukan.")
        print("")
    menu_admin()

def editmenuAd(barang):
    kode_barang = input("Masukkan kode barang yang ingin diedit: ")
    print("")
    found = False
    for item in barang:
        if item['kode'] == kode_barang:
            print(f"Barang dengan kode {kode_barang} ditemukan.")
            nama_barang = input("Masukkan nama baru untuk barang: ")
            item['Nama'] = nama_barang
            print(f"Nama barang berhasil diubah menjadi {nama_barang}.")
            found = True
            break
    if not found:
        print(f"Barang dengan kode {kode_barang} tidak ditemukan. Silakan coba lagi.")
    menu_admin()

def hapusmenuAd(barang):
    print(f"Data barang: {barang}")
    while True:
        kode_barang = input("Masukkan kode barang yang ingin Dihapus: ")
        found = False
        for item in barang:
            if item['kode'] == kode_barang:
                if not item['Nama']:
                    print("Barang sudah habis, mohon kembali ke menu dan tambahkan barang")
                    menu_admin()
                    break
                barang.remove(item)
                print(f"Barang dengan kode {kode_barang} telah dihapus.")
                found = True
                break
        if not found:
            print(f"Barang dengan kode {kode_barang} tidak ditemukan. Silakan coba lagi.")
            break
        else:
            break
    if not barang:
        print("Barang sudah habis, mohon kembali ke menu dan tambahkan barang")
        menu_admin()
    print(f"Data barang: {barang}")
    print("")
    menu_admin()


def lihatmenuUs(barang):
    print("========== Data Barang ==========")
    if not barang:
        print("Tidak ada barang dalam daftar.")
    else:
        for idx, item in enumerate(barang, start=1):
            print(f"{idx}. Nama: {item['Nama']}, Kode: {item['kode']}")
    print("")
    menu_user()

def carimenuUs(barang):
    search_value = input("Masukkan kode barang yang ingin Anda cari: ")
    found = False
    for item in barang:
        if item['Nama'] == search_value or item['kode'] == search_value:
            print(f"Barang dengan kode '{search_value}' memunculkan barang '{item['Nama']}'")
            found = True
            break
    if not found:
        print(f"Barang dengan kode '{search_value}' tidak ditemukan.")
    menu_user()

def keluarAd():
    keluar = input("Apakah anda yakin ingin keluar dari aplikasi? (Y/N): ")
    if keluar == "Y" or keluar == "y":
        print("========== TERIMA KASIH ==========")
        exit()
    elif keluar == "N" or keluar == "n":
        menu_admin()
    else:
        print("Invalid")
        print("")
        keluarAd()

def keluarUs():
    keluar = input("Apakah anda yakin ingin keluar dari aplikasi? (Y/N): ").lower()
    if keluar == "Y" or keluar == "y":
        print("========== TERIMA KASIH ==========")
        exit()
    elif keluar == "N" or keluar == "n":
        menu_user()
    else:
        print("Invalid")
        print("")
        keluarUs()
     
landing()