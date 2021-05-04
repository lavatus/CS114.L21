| Họ và tên      | MSSV | Lớp     |
| :---        |    :----:   |          ---: |
| Nguyễn Trung Tuấn  | 195222477      | CS114.L22.KHCL  |
| Dương Nguyễn Thuận | 195222312      | CS114.L22.KHCL  |
| Nguyễn Việt Thư    | 19522309       | CS114.L21.KHCL  |
# Bài tập tuần 6: 
*Câu hỏi quá trình:
Mỗi nhóm tìm dăm ba ví dụ về bài toán regression ***TRONG THỰC TẾ***
Ghi rõ input, output và cách thu thập + xử lý data, commit vào github repository và dẫn link lên đây.
Có thể ghi ra giấy rồi chụp hình hoặc viết ở dạng Markdown.*
## Ví dụ 1: Tìm được mối liên hệ giữa số tiền quảng cáo và lợi nhuận thu lại
* Inupt: số tiền quảng cáo và số tiền thu lại
* Output: số tiền y(...) thu lại từ việc bỏ ra x(...) quảng cảo, với ... là đơn vị tiền tệ tương ứng
* Cách thu thập: từ những lần quảng cáo (marketing) trước đó của công ty
* Xử lí: Loại bỏ những lần bỏ ra quá nhiều tiền nhưng lỗ
## Ví dụ 2: Đo lường sự ảnh hưởng của phân bón và nước đến năng suất trồng lúa
* Input: lượng nước, phân bón, các năng suất trồng lúa trước đó
* Output: Năng suất trồng lúa tương ứng với lượng nước và phân bón bỏ ra 
* Cách thu thập: Kết quả từ các bài báo nghiên cứu khoa học 
* Xử lí dữ liệu: Đưa dữ liệu(nước-lít, phân bón-kg) đoạn [0,1]
## Ví dụ 3: Để đo lường ảnh hưởng của các chế độ tập luyện khác nhau đối với năng suất của các cầu thủ bóng đá.
* Input: số buổi tập trong tuần, trọng lượng mỗi buổi tập, kết quả thi đấu
* Output : Kết quả thi đấu với bài tập tương ứng (Tìm ra được chế độ tập luyện thích hợp cho mỗi vận động viên để đạt kết quả thi đấu cao nhất)
* Cách thu thập: chế độ tập luyện được ghi lại qua mỗi lần tập và các kết quả thi đấu tương ứng, ví dụ 
* Xử lí dữ liệu: dùng PCA để giảm chiều dữ liệu
