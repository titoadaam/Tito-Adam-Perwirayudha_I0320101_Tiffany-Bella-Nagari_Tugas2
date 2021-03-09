#TITO ADAM PERWIRAYUDHA
#NIM I0320101
#KELAS C

invalid_input = True
print("\033[1;32;40m\n")
def start():
    question = input('''
    SELAMAT DATANG DI APLIKASI PENGHITUNG SERBAGUNA 2000!
    (made by Tito Adam P)


    Pilih Program:
    1) Menghitung Luas Persegi Panjang
    2) Menghitung Luas Lingkaran
    3) Menghitung Kubus
    4) Menghitung Konversi Suhu Celcius -> Farenheit
    5) Menghitung Konversi Reamur -> Kelvin

Program yang dipilih (masukan angka) = ''')

    if question == "1":
        print("""


        MENGHITUNG LUAS PERSEGI PANJANG

        """)
        panjang = int(input("Masukan PANJANG dari persegi panjang = "))
        lebar = int(input("Masukan LEBAR dari persegi panjang = "))

        luas_persegi_panjang = (panjang * lebar)

        print("Luas persegi panjang adalah = ", luas_persegi_panjang)
        print("======================================================")
    elif question == "2":
        print("""


                    MENGHITUNG LUAS LINGKARAN

                    """)
        question = input("""
        Diketahui : 
        1) JARI-JARI atau 
        2) DIAMETER
        Masukan Angka = """)
        if question == "1":
            jari_jari = int(input("Masukan JARI-JARI dari lingkaran = "))

            luas_lingkaran = (3.14 * jari_jari * jari_jari)

            print("Luas Lingkaran Adalah = ", luas_lingkaran)
            print("======================================================")
        elif question == "2":
            diameter = int(input("Masukan DIAMETER dari lingkaran = "))

            luas_lingkaran = (3.14 * diameter)

            print("Luas Lingkaran Adalah = ", luas_lingkaran)
            print("======================================================")
        else:
            print("""
            PROGRAM TIDAK DITEMUKAN (Hanya tersedia 1 - 2)

            ======================================================
                          !!!PROGRAM RESTARTING!!!
            ======================================================

            """)
    elif question == "3":
        print("""


                    MENGHITUNG KUBUS

                    """)
        question = input("""
        Pilih yang ingin di hitung : 
        1) Luas permukaan kubus
        2) Volume Kubus
        Masukan Angka = """)
        if question == "1":
            rusuk = int(input("Masukan PANJANG RUSUK dari kubus = "))

            luas_permukaan_kubus = (6 * rusuk * rusuk)

            print("Luas Permukaan Kubus = ", luas_permukaan_kubus)
            print("======================================================")
        elif question == "2":
            sisi = int(input("Masukan PANJANG RUSUK dari kubus = "))

            volume_kubus = (sisi * sisi * sisi)

            print("Volume Kubus Adalah = ", volume_kubus)
            print("======================================================")
        else:
            print("""
            PROGRAM TIDAK DITEMUKAN (Hanya tersedia 1 - 2)

            ======================================================
                          !!!PROGRAM RESTARTING!!!
            ======================================================

            """)
    elif question == "4":
        print("""


            MENGHITUNG CELCIUS -> FARENHEIT

            """)
        celcius = int(input("Masukan suhu CELCIUS = "))

        farenheit = ((9 * celcius / 5) + 32)

        print("Suhu Farenheit = ", farenheit)
        print("======================================================")
    elif question == "5":
        print("""


            MENGHITUNG REAMUR -> KELVIN

            """)
        reamur = int(input("Masukan suhu REAMUR = "))

        kelvin = ((5 * reamur / 4) + 273)

        print("Suhu Kelvin = ", kelvin)
        print("======================================================")
    else:
        print("""
        PROGRAM TIDAK DITEMUKAN (Hanya tersedia program 1 - 5)

        ======================================================
                      !!!PROGRAM RESTARTING!!!
        ======================================================

        """)
while invalid_input:
    start()