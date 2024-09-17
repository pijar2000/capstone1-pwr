# -----------------------------------------------------------------------------------------------------------------------
## data skor siswa

class Siswa:
    def __init__(self, id, nama, sex, tugas, UTS, UAS):
        self.id = id
        self.nama = nama
        self.sex = sex
        self.tugas = tugas
        self.UTS = UTS
        self.UAS = UAS

    def tampilkan_data(self):
        print(f"Id: {self.id}, Nama: {self.nama}, Jenis Kelamin: {self.sex}, Tugas: {self.tugas}, UTS: {self.UTS}, UAS: {self.UAS}")


class DASSI:
    def __init__(self):
        self.data_skor = [
            Siswa(1, 'number one', 'F', 81, 81, 81),
            Siswa(2, 'number two', 'M', 82, 82, 82),
            Siswa(3, 'number three', 'F', 83, 83, 83),
            Siswa(4, 'number four', 'M', 84, 84, 84),
        ]
        self.main_menu()

    def input_nomor(self):
        while True:
            id = input('\n    Input id Siswa (id): ')
            if id.isdigit():
                return int(id)
            print('\n    *****Penulisan Id tidak sesuai*****')


# Function 1----------------------------------------------------------------------------------------------------
## Read Data
    def read_data(self):
        print('''
        --------------DAFTAR SKOR SISWA-----------------

        1. Daftar Skor Siswa
        2. Daftar Skor Siswa Perorangan
        3. Main Menu
        ------------------------------------------------
        ''')

        option_sub = input('    sub-menu (1-3): ')

        if option_sub == '1':
            if not self.data_skor:
                print('\n    *****Data tidak tersedia!*****')
            else:
                print('\n    Daftar Skor Siswa:')
                for i, siswa in enumerate(self.data_skor, 1):
                    print(f"\t{i}. ", end="")
                    siswa.tampilkan_data()
        elif option_sub == '2':
            id = self.input_nomor()
            siswa = next((s for s in self.data_skor if s.id == id), None)
            if siswa:
                siswa.tampilkan_data()
            else:
                print('\n    *****Data tidak ditemukan!*****')
        elif option_sub == '3':
            self.main_menu()
        else:
            print('\n    *****Opsi tidak ada*****')

        self.read_data()


# Function 2----------------------------------------------------------------------------------------------------
## Create Data

    def create_data(self):
        print('''
        --------------TAMBAH DAFTAR SKOR SISWA---------------
        1. Tambah Data Skor Siswa
        2. Main Menu
        ----------------------------------------------------
        ''')

        option_sub = input('    Input sub-menu (1-2): ')

        if option_sub == '1':
            id = self.input_nomor()

            if any(siswa.id == id for siswa in self.data_skor):
                print("\n    *****Id sudah ada di Daftar Skor Siswa*****")
            else:
                nama = input('    Input nama siswa: ').title()
                while not (nama.isalpha() and len(nama) <= 30):
                    print("    *****Nama tidak valid! Harus huruf & maksimal 30 karakter.*****")
                    nama = input('    Input nama siswa: ').title()

                sex = input('    Input jenis kelamin siswa (M/F): ').upper()
                while sex not in ['M', 'F']:
                    print('    *****Jenis kelamin harus M/F*****')
                    sex = input('    Input jenis kelamin siswa (M/F): ').upper()

                tugas = int(input('    Input nilai tugas (0-100): '))
                UTS = int(input('    Input nilai UTS (0-100): '))
                UAS = int(input('    Input nilai UAS (0-100): '))

                siswa_baru = Siswa(id, nama, sex, tugas, UTS, UAS)
                self.data_skor.append(siswa_baru)
                print('\n    *****Data tersimpan*****')

        elif option_sub == '2':
            self.main_menu()
        else:
            print('\n    *****Opsi tidak valid!*****')

        self.create_data()

# Function 3----------------------------------------------------------------------------------------------------
## Update Data

    def update_data(self):
        print('''
        --------------UBAH DAFTAR SKOR SISWA---------------
        1. Ubah Skor Siswa
        2. Main Menu
        ----------------------------------------------------
        ''')

        option_sub = input('    Input sub-menu (1-2): ')

        if option_sub == '1':
            id = self.input_nomor()

            siswa = next((s for s in self.data_skor if s.id == id), None)
            if siswa:
                siswa.tampilkan_data()
                kolom = input('    Input kolom yang akan di-update [Id, Nama, Sex, Tugas, UTS, UAS]: ').lower()

                if kolom == 'id':
                    new_id = self.input_nomor()
                    if any(s.id == new_id for s in self.data_skor):
                        print("\n    *****Id sudah ada di Daftar Skor Siswa*****")
                    else:
                        siswa.id = new_id
                elif kolom == 'nama':
                    siswa.nama = input('    Input nama baru: ').title()
                elif kolom == 'sex':
                    siswa.sex = input('    Input jenis kelamin baru (M/F): ').upper()
                elif kolom in ['tugas', 'uts', 'uas']:
                    setattr(siswa, kolom, int(input(f'    Input nilai {kolom.upper()} baru (0-100): ')))
                print('    *****Data Terupdate!*****')
            else:
                print('\n    *****Data tidak ditemukan!*****')

        elif option_sub == '2':
            self.main_menu()
        else:
            print('\n    *****Opsi tidak valid!*****')

        self.update_data()


# Function 4----------------------------------------------------------------------------------------------------
## Delete Data

    def delete_data(self):
        print('''
        --------------HAPUS DAFTAR SKOR SISWA---------------
        1. Hapus Daftar Skor Siswa
        2. Main Menu
        ----------------------------------------------------
        ''')

        option_sub = input('    Input sub-menu (1-2): ')

        if option_sub == '1':
            id = self.input_nomor()
            siswa = next((s for s in self.data_skor if s.id == id), None)
            if siswa:
                self.data_skor.remove(siswa)
                print('\n    *****Data dihapus!*****')
            else:
                print('\n    *****Data tidak ditemukan!*****')
        elif option_sub == '2':
            self.main_menu()
        else:
            print('\n    *****Opsi tidak sesuai!*****')

        self.delete_data()


# Function 5-------------------------------------------------------------------------------------------------------------
## QUIT
    def quit_program(self):
        print('\n*****Terima kasih!*****')
        quit()

# -----------------------------------------------------------------------------------------------------------------------
## MAIN MENU
    def main_menu(self):
        print('''
        ----------------------DASSI----------------------------
        Selamat Datang di Daftar Skor Siswa Interface (DASSI) !

        Main Menu:
        1. Daftar Skor Siswa
        2. Tambah Daftar Skor Siswa
        3. Ubah Daftar Skor Siswa
        4. Hapus Daftar Skor Siswa
        5. Keluar dari Program DASSI
        -----------------PijarHM------------------------------
        ''')

        option_main = input('Input Main Menu (1-5): ')

        if option_main == '1':
            self.read_data()
        elif option_main == '2':
            self.create_data()
        elif option_main == '3':
            self.update_data()
        elif option_main == '4':
            self.delete_data()
        elif option_main == '5':
            self.quit_program()
        else:
            print('\n    *****Opsi tidak sesuai*****')
            self.main_menu()


# Memulai program
DASSI()
