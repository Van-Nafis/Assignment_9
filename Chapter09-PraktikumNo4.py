




import random
def shuffleString(x,n):
    x=list(x)
    data=[]
    while n>0:
        random.shuffle(x)
        data.append("".join(x))
        if n==0:
            break
        n=n-1
    print(data)
        

print("INPUT HURUF = ")
z=str(input())
print("INPUT PENGULANGAN = ")
a=int(input())
shuffleString(z,a)
