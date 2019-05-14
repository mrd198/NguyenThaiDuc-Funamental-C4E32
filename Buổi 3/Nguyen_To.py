n = int(input("Nhập số nguyên N:"))
while not 0 < n < 1000000:
    n = int(input("Nhập lại N trong khoảng từ 0 đến 1000000:"))

a = n
GT = []
while a != 1:
    for i in range(2,n): 
        if a % i == 0:
            GT.append(i)
            a = a/i
            break
print(n,"=",end=" ")
print(*GT,sep="*")