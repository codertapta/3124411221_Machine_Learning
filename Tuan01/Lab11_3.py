import torch
x = torch.tensor(
2.0,
requires_grad=True
)
y = 2*(x * x)+3*x+5
y.backward()
print("x =", x)
print("y =", y)
print("x.grad =", x.grad)