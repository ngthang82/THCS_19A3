a = float(input("Nhập lãi suất 1 năm: "))
b = float(input("Nhập số tiền gửi: "))
tien_lai_1_thang = b*(a/100)*1/12
tien_lai_2_quy = b*(a/100)*1/2
tien_lai_3_nam = b*(a/100)*3
print(f"Tiền lãi sau 1 tháng: {tien_lai_1_thang:.2f}")
print(f"Tiền lãi sau 2 quý: {tien_lai_2_quy:.2f}")
print(f"Tiền lãi sau 3 năm: {tien_lai_3_nam:.2f}")