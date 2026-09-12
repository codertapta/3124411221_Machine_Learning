import numpy as np
import torch
#Hàm polyd cho tạo thành đa thức từ số cho vào
#Với trường hợp này 1,2,3 có nghĩa 1x^2+2x+3
polynomial = np.poly1d([1, 2, 3])
#Tạo mẫu thử, có 20 mẫu thử
N = 20
#Tạo ngẫu nhiên ma trận 20 hàng 1 cột và nhân giá trị của phần từ cho 5
X = np.random.randn(N, 1) * 5
#Thế x vào đa thức trên để thu kết quả có 20 x đồng nghĩa có 20 giá trị y
Y = polynomial(X)
# Lúc này là tính trên đa thức bây giờ ta sẽ tính trên tensor với X^2 + 2X^2+3
#Nên cần X ta đã có ở dòng 9
#Tạo X^2 bằng cách lấy X*X
#Tạo hệ số c trong ax^2+bx+c bằng lệnh np.ones_like(X)
#Tức là tạo 1 cái có cấu tạo giống X nhưng tất cả giá trị=1
#sau đó ghép x x^2 và 1 lại bằng hstack từ đó thành 1 ma trận với cột đầu là giá trị x^2 cột 2 là x và cột 3 là 1

XX = np.hstack([
X * X,
X,
np.ones_like(X)
])
#Sau đó tạo ngẫu nhiên 3 hệ số a,b,c lưu vào w
#Ta tạo tensor x là ma trận xx nãy vừa tạo
#ta tạo tensor y 
#Sau đó ta dự tính cập nhật w với tốc độ 0.01 sau mỗi lần sai
w = torch.randn(3, 1, requires_grad=True)
x = torch.tensor(XX, dtype=torch.float32)
y = torch.tensor(Y, dtype=torch.float32)
optimizer = torch.optim.NAdam([w], lr=0.01)
#In w lần đầu tiên để so sánh
print("Initial coefficients:")
print(w)
#Thử học và cập nhật 1000 lần
for epoch in range(1000):
 #Xóa cập nhật w cũ
 optimizer.zero_grad()
 #Tính y dự đoán từ ma trận xx và hệ số w ngẫu nhiên 
 y_pred = x @ w
 #Tính sai số bình phương trung bình bằng cách lấy y thật - y dự đoán
 mse = torch.mean(torch.square(y - y_pred))
 #Tính sai số của w
 mse.backward()
 #Dựa vào sai số để cập nhật w
 optimizer.step()
print("Learned coefficients:")
print(w)