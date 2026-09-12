import random
import torch
A = torch.tensor(random.random(), requires_grad=True)
B = torch.tensor(random.random(), requires_grad=True)
C = torch.tensor(random.random(), requires_grad=True)
D = torch.tensor(random.random(), requires_grad=True)
EPOCHS = 2000
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
optimizer = torch.optim.NAdam([A, B, C, D], lr=0.01)
for _ in range(EPOCHS):
 #Bài toán cố gắng cho y1->4=0 để A+B=9,... để tìm ra A,B,C,D
 y1 = A + B - 9
 y2 = C - D - 1
 y3 = A + C - 8
 y4 = B - D - 2
#Tính tổng bình phương của sqeer để xem ABCD ảnh hưởng thế nào đến nó sao đó cập nhật ABCD
 sqerr = y1*y1 + y2*y2 + y3*y3 + y4*y4
 optimizer.zero_grad()
 sqerr.backward()
 optimizer.step()
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)