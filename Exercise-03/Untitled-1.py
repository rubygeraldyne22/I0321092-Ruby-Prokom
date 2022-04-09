print("================================================")
kelas = ['Ali', 'Budi', 'Caca', 'Dinda', 'Elo', 'Bayu', 'Adi', 'Nina']

kelas.append("Siska")
kelas.append("Maya")
kelas.insert(3, "Zasa")

print(len(kelas))
print("=========================")
for i in range (0,len(kelas)):# urutkan murid sebanyak data jumlah murid
    print("no murid=", i, "  ", kelas[i])
print("==========================")