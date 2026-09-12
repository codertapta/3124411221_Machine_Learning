import torch

a = torch.randn(3, 4, 5)

print("Tensor:")
print(a)

print("Tensor a[1]:")
print(a[1])

print("Tensor a[1:, 2:4]")
print(a[1:, 2:4])

print("Hai phần tử cuối của chiều thứ 3:")
print(a[:, :, 3:5])