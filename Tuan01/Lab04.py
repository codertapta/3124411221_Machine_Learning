import torch
a=torch.randn(3,4,5)
print("Tensor:")
print(a)
#Slicing a[1]: là in cá giá trị của khối 1,Tensor trên có 3 khối 0,1,2 a[1] là in giá trị của khối 1
print("Tensor a[1]:")
print(a[1])
#Index bao gồm a[x1:y1, x2:y2, x3:y3]
#Trong đó x1:y1 nghĩa là chọn khối để in ví dụ 1:2 là in khối 1->2 còn trong bài 1: nghĩa là in khối từ 1 tới hết
#x2:y2 là chọn hàng để in khi 2:4 tức là in hàng 2,3
#x3:y3 là chọn cột để in
print("Tensor a[1:,2:4]")
#Khi in ra sẽ có 2 khối do chọn khối in từ 1 tới hết và mỗi khối chỉ hiển thị hàng 2,3 của khối đó
print(a[1:,2:4])
print("Hai phần từ cuối của chiều thứ 3:")
print(a[:, :,3:5])
