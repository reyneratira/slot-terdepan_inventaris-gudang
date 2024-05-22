# Define the users and their passwords
users = {
    "admin": "password123"
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
    

def menu_user():
    print("========== MENU USER ==========")
    print("1. Lihat Barang")
    print("2. Cari Barang")


# Call the login function to start the login process
landing()