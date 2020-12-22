def bintang():
    print("Mau berapa baris?")
    baris=int(input())
    i=0
    j=2
    while i<=baris:
        if i<(baris//2):
            print(("*"+"**"*i).center(baris*2))
            i=i+1
        if i==(baris//2):
            print(("*"+"**"*i).center(baris*2))
            i=i+1
        if i>(baris//2):
            print(("*"+"**"*(i-j)).center(baris*2))
            i=i+1
            j=j+2
        if i==baris:
            break


bintang()
