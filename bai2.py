hoten = str(input('Xin chào! Hãy nhập tên đầy đủ bên dưới:\n'))
while hoten == '':
    hoten = str(input('Xin nhập lại họ tên:\n'))
ten_list = [i.capitalize() for i in hoten.split()]
hoten = ' '.join(ten_list)
ten = ten_list.pop(-1)
if len(ten_list) > 0:
    ho = ten_list.pop(0)
    if len(ten_list) > 0:
        tenlot = ' '.join(ten_list)
    else:
        tenlot = ''
else:
    tenlot,ho = '',''
print('Chúc bạn {} một ngày tốt lành.'.format(ten))
f = open('danhsachten.csv',mode='a',encoding='UTF8')
f.write('{},{},{},{}\n'.format(hoten,ho,ten,tenlot))
f.close()


# Viết một chương trình với mô tả sau
# Khi chạy chương trình sẽ hiện ra như sau

#  Xin chào! Hãy nhập tên đầy đủ bên dưới (gõ luôn cả dấu tiếng Việt nha)
#  -

# Người dùng sẽ nhập họ tên đầy đủ của mình sau đó chương trình sẽ làm các việc sau
# Tính toán để lấy được họ, tên và chữ lót
# Sau đó hiện ra câu
#  Chúc bạn <tên đã nhận ra được> một ngày tốt lành!

# Rồi lưu vào file danhsachten.csv thêm một line với format sau 
#  chuỗi họ tên, chuỗi họ, chuỗi tên, chuỗi chữ lót [và xuống dòng]

# ví dụ anh nhập vào Trần Xuân Ngọc Tân thì chương trình sẽ xuất câu "Chúc bạn Tân một ngày tốt lành"
# đồng thời lưu thêm 1 dòng vào file có nội dung sau "Trần Xuân Ngọc Tân, Trần, Tân, Xuân Ngọc"

# Thử suy nghĩ xem nếu user nhập lung tung vào thì họ sẽ nhập những gì và chương trình của mình sẽ đối phó như thế nào
