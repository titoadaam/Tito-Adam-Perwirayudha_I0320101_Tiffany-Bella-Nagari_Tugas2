#TITO ADAM PERWIRAYUDHA
#NIM I0320101
#KELAS C
print("APLIKASI PENGECEKAN BERAT BADAN")
nama = str(input("Masukan Nama Anda = "))
umur = int(input("Masukan Umur Anda = "))
tinggi = float(input("Masukan Tinggi Badan Anda = "))
berat_badan = float(input("Masukan Berat Badan Anda = "))
question = input('''
Jenis Kelamin
1) Laki-laki
2) Perempuan

Pilih Jenis Kelamin (masukan angka) = ''')
if question == "1":
    kelamin = "Laki-laki"
elif question == "2" :
    kelamin = "perempuan"
else :
    print("ERROR (CEK KEMBALI PENGISIAN KELAMIN!)")
print("\033[1;32;40m\n")
print("""=======DATA DIRI========""")
print ((nama), (umur),("Tahun "), (tinggi),("cm "), (berat_badan), ("KG "), (kelamin))
if kelamin == "Laki-laki" :
    berat_badan_ideal = abs(tinggi - 100 - (tinggi - 100) * 10 / 100)
    if berat_badan_ideal < berat_badan :
        print("Turunkan Berat Badan!")
    elif berat_badan_ideal == berat_badan :
        print("Pertahankan Dan jaga Berat Badan Mu!")
    else :
        print("Naikan Berat Badan")
else :
    berat_badan_ideal = (tinggi - 100 - (tinggi - 100) * 15 / 100)
    if berat_badan_ideal < berat_badan:
        print("Turunkan Berat Badan!")
    elif berat_badan_ideal == berat_badan:
        print("Pertahankan Dan jaga Berat Badan Mu!")
    else:
        print("Naikan Berat Badan")
print (("Berat Badan Ideal Anda = "), berat_badan_ideal,("KG"))