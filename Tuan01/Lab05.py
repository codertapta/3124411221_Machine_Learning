import torch
a=torch.randn(3,4)
print("Tensor:")
print(a)
print("Số phần tử trước khi reshape:",a.numel())
#ravel là biến các tensor thành 1 chiều 
print("Flatten(Làm phẳng:)")
print(a.ravel())
print("Reshape")
#Biến đổi kích cỡ mà không cần tạo lại
print(a.reshape(3,2,2))
print("Số phần từ sau khi reshape:",a.numel())
print("Đổi thành 2x6:")
print(a.reshape(2,6))
