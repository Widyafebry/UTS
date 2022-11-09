
def Menu():
    X = "Capucino"
    Y = "Teh"
    print ("pilihan")
    print ("1.", X)
    print ("2.", Y)
    print ("3.", exit)

def data():
    nim = (input("NIM : "))
    nama = (input("Nama : "))

def capucino():
    X = "memilih Capucino"
    print (X)
    harga = int(input("Masukan Harga : "))
    pembayaran = harga + (harga * 10/ 100)
    print ("Jumlah yang harus dibayar : ", pembayaran)

while True:
    data()
    Menu()
    choice = int(input("Masukan Pilihan : "))
    if choice == 1:
        capucino()
    elif choice == 2:
        Teh()
    elif choice == 3:
        break
    else:
        print ("pilihan salah")