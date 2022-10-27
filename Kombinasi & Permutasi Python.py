#Langkah 1 : input nilai
k=int(input('Input k : '))
n=int(input('Input n : '))

#Langkah 2 : perhitungan permutasi
list1=[]
i=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
        hasilpermu=(n-i)
        list1.append(hasilpermu)
        i+=1
        if ((n-i)+k)==n:
            break

#Langkah 3 : perhitungan kombinasi
list2=[]
j=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
        hasilkombi=(k-j)
        list2.append(hasilkombi)
        j+=1
        if (k-j)==0:
            break

#Langkah 4 : Menghitung Hasil

def hasil(data):
    r=1
    for x in data:
        r=r*x
    return r

#Langkah 5 : Hasil

print(f'P({n},{k})={hasil(list1)}')
print(f'C({n},{k})={hasil(list1)/hasil(list2)}')
