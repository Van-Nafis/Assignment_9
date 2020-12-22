mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("============================================================")
print("NIM\tNAMA MAHASISWA\t\tTGL LAHIR\tTEMPAT LAHIR")
print("------------------------------------------------------------")

z=0
datatanggal=[]
for i in mhs:
    i=mhs[z].split(":")
    z=z+1
    datatanggal.append(i)

b=0
datatanggal2=[]
for j in datatanggal:
    j=datatanggal[b][2].split("-")
    b=b+1
    datatanggal2.append(j)

j=mhs[0].split(":")
print(j[0],"\t",j[1],"\t\t",datatanggal2[0][2]+"/"+datatanggal2[0][1]+"/"+datatanggal2[0][0],"\t",j[3])
j=mhs[1].split(":")
print(j[0],"\t",j[1],"\t",datatanggal2[1][2]+"/"+datatanggal2[1][1]+"/"+datatanggal2[1][0],"\t",j[3])
j=mhs[2].split(":")
print(j[0],"\t",j[1],"\t\t",datatanggal2[2][2]+"/"+datatanggal2[2][1]+"/"+datatanggal2[2][0],"\t",j[3])

