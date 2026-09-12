import torch
#Khởi tạo x=3.6
x = torch.tensor(
3.6,
#Yêu cầu torch theo dõi tensor này
requires_grad=True
)
y = x * x
#Gọi .backward mới có thể dùng x.grad và x.grad thể hiện độ lệch của x và y
#ví dụ x=3 y=9 với y=x^2. Sau đó  nếu x=3.01 thì y=9.0601 cái độ tỉ lệ giữa x và y là x.grad
y.backward()
print("x =", x)
print("y =", y)
print("x.grad =", x.grad)
z= 3*x**2 + 2*x + 1
z.backward()
print("x.grad phương trình thứ 2:",x.grad)