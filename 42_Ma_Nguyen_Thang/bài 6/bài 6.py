nam = int(input("Nhập năm muốn kiểm tra: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")