import requests
import bs4
import pyexcel
from youtube_dl import YoutubeDL

#lấy html liệu từ Itunes
data = requests.get('https://www.apple.com/itunes/charts/songs/')
html = data.content.decode()

options = {'default_search': 'ytsearch','max_downloads': 50}
dl = YoutubeDL(options)

#Tạo đối tượng soup để xử lý dữ liệu dạng html
soup = bs4.BeautifulSoup(html,"html.parser")
# Liệt kê danh sách bài hát nằm trong thẻ li nằm trong section có thuộc tính section chart-grid
search = soup.find("section",{"class":"section chart-grid"}).find_all("li")
ket_qua = []

for v in search:
    DSbai_hat = {}
    DSbai_hat['Thứ hạng'] = v.strong.text
    DSbai_hat['Names'] = v.h3.text
    DSbai_hat['Artists'] = v.h4.text
    ket_qua.append(DSbai_hat)
    # Thực hiện download 
    # ket_qua.append(DSbai_hat)
    # dl.download([v.h3.string+""+v.h4.string])
    

#In kết quả ra màn hình
for i in ket_qua:
    print(i['Thứ hạng'],":",i['Names'],"of",i['Artists'])

# Thực hiện in kết quả ra file excel
pyexcel.save_as(records=ket_qua, dest_file_name="Itunes top songs.xlsx")


