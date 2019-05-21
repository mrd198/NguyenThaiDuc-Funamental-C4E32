def is_inside(toa_do_diem,hinh):
    if hinh[0] < toa_do_diem[0] < hinh[0] + hinh[2] and hinh[1] < toa_do_diem[1] < hinh[1] + hinh[3]:
        return True
    else:
        return False
x = int(input("Nhập tọa độ x của điểm:"))
y = int(input("Nhập tọa độ y của điểm:"))
a = int(input("Nhập vị trí a của hình:"))
b = int(input("Nhập vị trí b của hình:"))
c = int(input("Nhập chiều dài cạnh 1 của hình:"))
d = int(input("Nhập chiều dài cạnh 2 của hình:"))
if True:
    print("Điểm vừa nhập nằm trong hình")
else:
    print("Điểm vừa nhập không nằm trong hình")
is_inside([x,y],[a,b,c,d])