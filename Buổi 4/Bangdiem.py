danh_sach = [
    {
    'Tên':'Nguyễn Thái Đức','Tuổi': '18','Điểm toán':7,'Điểm lý':10,'Điểm hóa':6,'Sđt': ['0378408181','0396240614'],'Địa chỉ':"Hà Nội",
    },
    {
    'Tên': 'Nguyễn Thị Dung','Tuổi': '18', 'Điểm toán':8,'Điểm lý':8,'Điểm hóa':9,'Sđt': ['0876325543'],'Địa chỉ':"Nghệ An",
    },
    {
    'Tên': 'Trần Đức Nghĩa','Tuổi': '18','Điểm toán':5,'Điểm lý':6,'Điểm hóa':8,'Sđt': ['0876325543'],'Địa chỉ':"Yên Bái",
    },
    {
    'Tên': 'Nguyễn Minh Đức','Tuổi': '20','Điểm toán':9,'Điểm lý':8,'Điểm hóa':7,'Sđt': ['012345678'],'Địa chỉ':"Lào Cai",
    },
    {
    'Tên': 'Lê Thị Dung','Tuổi': '18','Điểm toán':10,'Điểm lý':6,'Điểm hóa':7,'Sđt': ['0377844523'],'Địa chỉ':"Hải Phòng",
    }
]
# In ra học sinh có điểm toán cao nhất
diem_cao_toan = 0
ten = []
for p in danh_sach:
    if p['Điểm toán'] > diem_cao_toan:
        if p['Điểm toán'] > diem_cao_toan:
            ten.clear()
        diem_cao_toan = p['Điểm toán']
        ten.append(p['Tên'])
print("Học sinh có điểm toán cao nhất là:",*ten," với",diem_cao_toan,"điểm")

# In ra điểm trung bình của tất cả học sinh
for p in danh_sach:
    diemtb = ((p['Điểm toán']+p['Điểm lý']+p['Điểm hóa'])/3)
    print("Điểm trung bình của học sinh",p['Tên'],"là:",diemtb)

# Nhập số đt và hiển thị tên hs có sđt đó
sdt = input("Nhập số đt: ")
ten_sdt = []
for p in danh_sach:
    if sdt in p['Sđt']:
        ten_sdt.append(p['Tên'])
if len(ten_sdt) != 0:  
    print(*ten_sdt)
else:
    print("Không có tên  và số điện thoại")
