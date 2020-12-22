nilai=[{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
       {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
       {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
       {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
       {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("===================================================")
print("NIM",end="")
print("NAMA".rjust(10),end="")
print("N.MID".rjust(15),end="")
print("N.UAS".rjust(20))
print("---------------------------------------------------")
print(str(nilai[0]["nim"]),str(nilai[0]["nama"]).ljust(8),str(nilai[0]["mid"]).rjust(15),str(nilai[0]["uas"]).rjust(20))
print(str(nilai[1]["nim"]),str(nilai[1]["nama"]).ljust(8),str(nilai[1]["mid"]).rjust(15),str(nilai[1]["uas"]).rjust(20))
print(str(nilai[2]["nim"]),str(nilai[2]["nama"]).ljust(8),str(nilai[2]["mid"]).rjust(15),str(nilai[2]["uas"]).rjust(20))
print(str(nilai[3]["nim"]),str(nilai[3]["nama"]).ljust(8),str(nilai[3]["mid"]).rjust(15),str(nilai[3]["uas"]).rjust(20))
print(str(nilai[4]["nim"]),str(nilai[4]["nama"]).ljust(8),str(nilai[4]["mid"]).rjust(15),str(nilai[4]["uas"]).rjust(20))
