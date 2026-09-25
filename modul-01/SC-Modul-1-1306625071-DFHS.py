# Program Konversi Suhu Celcus-Reamur-Fahrenheit

# Header dan Input Identitas
print("Program Konversi Suhu\n")
print("Nama : Desintan Feby Harum Saragih")
print("NIM : 1306625071")
print()

#  Input Parameter  Suhu
suhu_awal = float(input("Suhu awal = "))
suhu_akhir = float(input("Suhu akhir = "))
selang =float(input("selang = "))
print()

# Header Tabel
print("TABEL KONVERSI")
print(f"{'No.' :<4} | {'Celcius':<10} | {'Reamur':<10} | {'fahrenheit':<10}")
print("-" * 45)

# Insialisasi Variabel Perulangan
c = suhu_awal
no = 1


# Perulangan while untuk Perhitungan dan Cetak Format Tabel
while c <= suhu_akhir:
    r = 0.8 * c
    f = (1.8 * c) + 32

    # Cetak baris tebal dengan format rapi
    print(f"{no:<4} | {c:<10.1f} | {r:<10.1f} | {f:<10.1f}")

    c += selang
    no += 1

