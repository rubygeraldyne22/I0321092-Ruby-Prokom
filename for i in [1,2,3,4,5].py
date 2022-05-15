print("============================")
angka =int(input("Masukkan nilai dasar angka="))
pangkat =int(input("Masukkan nilai dasar pangkat="))
y = 1

#melakukan looping
while (pangkat != 0):
    y = y * angka
    pangkat=pangkat-1
print("hasil pangkat =", y)