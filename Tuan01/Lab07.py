import torch
a=torch.randn(3,4)
print(a)
print("\nMean:")
#Mean là giá trị trung bình
print(torch.mean(a, dim=0))
#Độ lệch chuẩn
print("\nStandard deviation:")
print(torch.std(a, dim=0))
#Tính tổng
print("\nCumulative sum:")
print(torch.cumsum(a, dim=0))
#Còn dim=0 là theo chiều Trên xuống dưới, dim=1 là theo chiều trái sang phải, dim=2 là chỉ có khi 3 chiều
print(torch.mean(a, dim=1))
print(torch.std(a, dim=1))
print(torch.cumsum(a, dim=1))


