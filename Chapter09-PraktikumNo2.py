def bintang():
    print("Mau berapa baris?")
    baris=int(input())
    i=0
    while True:
        if i<(baris//2):
            print(("*"+"**"*i).center(baris*2))
            i=i+1
        elif i==baris:
            print(("*"+"**"*i).center(baris*2))
            i=i+1
        elif i>(baris//2):
            print(("*"+"**"*i).center(baris*2))
            i=i+1
        else:
            break


bintang()



