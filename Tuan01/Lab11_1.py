import torch
X=torch.randn(24)
print(X)
print("Đổi thành 4x6")
print(X.reshape(4,6))
print("Đổi thành 2x12")
print(X.reshape(2,12))
print("Đổi thành 2x3x4")
print(X.reshape(2,3,4))