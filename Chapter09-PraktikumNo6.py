nilai=[{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
       {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 80}, 
       {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
       {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
       {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("=======================================================================")
print("NIM",end="")
print("NAMA".rjust(9),end="")
print("N.MID".rjust(12),end="")
print("N.UAS".rjust(14),end="")
print("N.AKHIR".rjust(16),end="")
print("STATUS".rjust(18))
print("-----------------------------------------------------------------------")

p = 0
nakhir = []
for i in nilai:
    j = (nilai[p]["mid"] + 2 * nilai[p]["uas"]) / 3
    nakhir.append(j)
    p = p + 1



def status(x):
    if x > 60:
        print("LULUS".rjust(17))
    else:
        print("TIDAK LULUS".rjust(17))

print(str(nilai[0]["nim"]),str(nilai[0]["nama"]).ljust(8),str(nilai[0]["mid"]).rjust(10),str(nilai[0]["uas"]).rjust(12),str(nakhir[0]).rjust(15),str(status(nakhir[0])))
print(str(nilai[1]["nim"]),str(nilai[1]["nama"]).ljust(8),str(nilai[1]["mid"]).rjust(10),str(nilai[1]["uas"]).rjust(12),str(nakhir[1]).rjust(15),str(status(nakhir[1])))
print(str(nilai[2]["nim"]),str(nilai[2]["nama"]).ljust(8),str(nilai[2]["mid"]).rjust(10),str(nilai[2]["uas"]).rjust(12),str(nakhir[2]).rjust(15),str(status(nakhir[2])))
print(str(nilai[3]["nim"]),str(nilai[3]["nama"]).ljust(8),str(nilai[3]["mid"]).rjust(10),str(nilai[3]["uas"]).rjust(12),str(nakhir[3]).rjust(15),str(status(nakhir[3])))
print(str(nilai[4]["nim"]),str(nilai[4]["nama"]).ljust(8),str(nilai[4]["mid"]).rjust(10),str(nilai[4]["uas"]).rjust(12),str(nakhir[4]).rjust(15),str(status(nakhir[4])))


