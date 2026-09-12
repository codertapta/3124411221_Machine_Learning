import torch
#Tạo tensor ngẫu nhiên với 3 hàng và 4 cột
#rand không tạo ra số âm nhưng randn có thể
a=torch.rand(3,4)
e=torch.randn(3,4)
#Tạo tensor với giá trị 0 với 2 hàng và 3 cột
b=torch.zeros(2,3)
#Tạo tensor với giá trị 1 với 2 hàng và 3 cột
c=torch.ones(2,3)
#Tạo tensor là ma trận đơn vị với 3 hàng và 3 cột
d=torch.eye(3,3)
print(a)
print(b)
print(c)
print(d)
print(e)