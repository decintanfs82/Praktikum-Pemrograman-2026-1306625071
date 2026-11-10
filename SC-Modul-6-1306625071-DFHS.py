
import random

print("Permainan Tebak Nama Buah")
print("Oleh : Desintan Feby Harum Saragih")
print("NIM  : 1306625071")

databuah = [
    'anggur', 'apel', 'aprikot', 'asam', 'atap', 'arbei',
    'abiu', 'alpukat', 'anjeng', 'bacang', 'baguk',
    'belimbing', 'bengkuang', 'benda', 'binjai', 'bisbul',
    'blueberry', 'burahol', 'blewah', 'bit', 'cempedak',
    'ceplukan', 'cermai', 'ceri', 'cokelat', 'delima',
    'duku', 'durian', 'duwet', 'enau', 'enam-enam',
    'frambos', 'hamoi', 'hamlam', 'holdi', 'jamblang',
    'jambuair', 'jambubatu', 'jambubol', 'jambumawar',
    'jambumede', 'jengkol', 'jeruk', 'jerukbali',
    'jerukkeprok', 'jerukklingkit', 'jeruknipis',
    'jerukpurut', 'kapulasan', 'kawista', 'kecapi',
    'kedondong', 'kelapa', 'kelengkeng', 'kelubi',
    'ketela', 'kemang', 'kepel', 'kersen', 'kesemek',
    'kokosan', 'kiwi', 'koldi', 'kurma', 'kelawi',
    'kenitu', 'lai', 'langsat', 'lemon', 'leci',
    'lobak', 'maja', 'malaka', 'mangga', 'manggis',
    'markisa', 'melon', 'mengkudu', 'menteng', 'matoa',
    'mentimun', 'namnam', 'nanas', 'nangka', 'naga',
    'nona', 'pepaya', 'persik', 'pir', 'pisang', 'pete',
    'rambai', 'rambusa', 'rambutan', 'rukem', 'sawo',
    'semangka', 'sirsak', 'siwalan', 'srikaya',
    'stroberi', 'sukun', 'terap', 'terong', 'tomat',
    'timunsuri', 'ubi', 'waluh', 'wuni', 'zaitun'
]

while True:

    buah = random.choice(databuah)
    L = len(buah)
    N = L
    n = N

    jawaban = ['-'] * L

    print("\nKomputer sedang memikirkan nama buah terdiri dari", L, "huruf.")
    print("Nama buah :", " ".join(jawaban))

    while n > 0 and '-' in jawaban:

        print("\nAnda memiliki", n,
              "kesempatan untuk menebak huruf buah tersebut.")

        f = input("Tebakan anda ? ").lower()

        ketemu = False

        for i in range(L):
            if buah[i] == f:
                jawaban[i] = f
                ketemu = True

        if ketemu == True:
            print("Benar. Huruf", f,
                  "ada dalam nama buah tersebut.")
        else:
            print("Sayang sekali. Huruf", f,
                  "tidak ada dalam nama buah tersebut.")
            n = n - 1

        print("Nama buah :", " ".join(jawaban))

    if '-' not in jawaban:
        print("\nSELAMAT. Anda berhasil !!")
    else:
        print("\nGAME OVER !!")
        print("Nama buah yang benar adalah", buah)

    ulang = input("\nMau main lagi (y/t) ? ").lower()

    if ulang != 'y':
        print("# SELESAI #")
        break
