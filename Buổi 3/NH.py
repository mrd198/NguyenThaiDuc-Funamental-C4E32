Tien_gui = 21
Lai_suat = 6.5 / 100
for i in range(9):
    Tien_gui = Tien_gui + Tien_gui * Lai_suat
print("sau 9 nam co :",Tien_gui,"trieu")
Tien_gui = 21
Nam = 0
while Tien_gui < 1200:
    Tien_gui = Tien_gui + Tien_gui * Lai_suat
    Nam += 1
print("Sau",Nam,"nam thi mua duoc nha")