#TITO ADAM PERWIRAYUDHA
#NIM I0320101
#KELAS C
#SOAL LATIHAN NOMOR 2
invalid_input = True
print("\033[1;32;40m\n")
def start():
    question = input('''
    SELAMAT DATANG DI APLIKASI PENGHITUNG SERBAGUNA 2000!


    Pilih Program:
    1) Menghitung Luas Dan Keliling Persegi Panjang
    2) Menghitung Luas Dan Keliling Lingkaran
    3) Menghitung Luas Dan Volume Kubus
    4) Menghitung Konversi Suhu Celcius -> Farenheit
    5) Menghitung Konversi Reamur -> Kelvin

Program yang dipilih (masukan angka) = ''')
    if question == "1":
        print("""


        MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG

        """)

        panjang = int(input("Masukan PANJANG dari persegi panjang = "))
        lebar = int(input("Masukan LEBAR dari persegi panjang = "))

        luas_persegi_panjang = (panjang * lebar)
        keliling_persegi_panjang = ((panjang + lebar) * 2)

        print("Luas persegi panjang adalah = ", luas_persegi_panjang)
        print("Keliling persegi panjang adalah = ", keliling_persegi_panjang)
        print("======================================================")
    elif question == "2":
        print("""


        MENGHITUNG LUAS DAN KELILING LINGKARAN

                    """)
        jari_jari = int(input("Masukan JARI-JARI dari lingkaran = "))

        luas_lingkaran = (3.14 * jari_jari * jari_jari)
        keliling = (2 * 3.14 * jari_jari)

        print("Luas Lingkaran Adalah = ", luas_lingkaran)
        print("Keliling Lingkaran Adalah = " , keliling)
        print("======================================================")
    elif question == "3":
        print("""


                    MENGHITUNG LUAS DAN VOLUME KUBUS

                    """)
        rusuk = int(input("Masukan PANJANG RUSUK dari kubus = "))

        luas_permukaan_kubus = (6 * rusuk * rusuk)
        volume_kubus = (rusuk * rusuk * rusuk)

        print("Volume Kubus Adalah = ", volume_kubus)
        print("Luas Permukaan Kubus = ", luas_permukaan_kubus)
        print("======================================================")
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