# Define the users and their passwords
users = {
    "admin": "123"
}

barang = {
    "Kursi" : "1",
    "Meja" : "2",
    "Sofa" : "3",
    "Kasur" : "4"
}

def landing():
    print("Selamat Datang Di Aplikasi Inventaris Gudang!!")
    while True:
        print("Anda Ingin Masuk Sebagai : ")
        print("1. Admin")
        print("2. User")

        try :
            pilihan = int(input("Masukkan Pilihan Anda: "))
            if pilihan == 1:
                login()
                break
            elif pilihan == 2:
                menu_user()
                break
            else:
                print("Silahkan Pilih Sesuai Yang Tertera")
        except(ValueError):
            print("Masukan Angka Sesuai Pilihan yang tertera")
        
    

# Function to check if the user exists and the password is correct
def check_user_password(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

# Function to handle the login process
def login():
    print("Welcome to the login system!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user exists and the password is correct
    if check_user_password(username, password):
        print("Login successful!")
        print("Welcome Admin!!")
        menu_admin()
    else:
        print("Invalid username or password. Please try again.")

def menu_admin():
    print("========== MENU ADMIN ==========")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Edit Barang")
    print("4. Cari Barang")
    print("5. Hapus Barang")
    print("6. Keluar")
    pil_menu = int(input("Masukan Angka Pilihan Yang Tertera : "))

    if pil_menu == 1 :
        lihatmenuAd(barang)
    elif pil_menu == 2 :
        print("Tambah Menu")
    elif pil_menu == 3 :
        print("Edit Menu")
    elif pil_menu == 4 :
        carimenuAd(barang)
    elif pil_menu == 5 :
        print("Hapus Menu")
    elif pil_menu == 6 : 
        print("========== TERIMA KASIH ==========")
        exit
    else:
        print("Pilihan Invalid, Mohon Input Ulang")
        menu_admin()

def menu_user():
    print("========== MENU USER ==========")
    print("1. Lihat Barang")
    print("2. Cari Barang")
    print("3. Keluar") 
    pil_menus = int(input("Masukan Angka Pilihan Yang Tertera : "))

    if pil_menus == 1:
        lihatmenuUs(barang)
    elif pil_menus == 2:
        carimenuUs(barang)
    elif pil_menus == 3:
        print("========== TERIMA KASIH ==========")
        exit
    else:
        print("Pilihan Invalid, Mohon Input Ulang")
        menu_user()

def lihatmenuAd(barang):
    print(f"Data Barang: {barang}")
    menu_admin()

def carimenuAd(barang):
    search_value = input("Masukkan nam/kode barang yang ingin Anda cari: ")
    if search_value in barang.values():
        print(f"Barang '{search_value}' ditemukan dengan kode '{next(key for key, value in barang.items() if value == search_value)}'.")
    else:
        print(f"Barang dengan nama '{search_value}' tidak ditemukan.")
    menu_admin()

def lihatmenuUs(barang):
    print(f"Data Barang: {barang}")
    menu_user()

def carimenuUs(barang):
    search_value = input("Masukkan nam/kode barang yang ingin Anda cari: ")
    if search_value in barang.values():
        print(f"Barang '{search_value}' ditemukan dengan kode '{next(key for key, value in barang.items() if value == search_value)}'.")
    else:
        print(f"Barang dengan nama '{search_value}' tidak ditemukan.")
    menu_user()


# Call the login function to start the login process
landing()