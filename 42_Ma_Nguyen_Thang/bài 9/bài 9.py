kwh = float(input("Nhập tổng số kWh đã tiêu thụ: "))
gia_bac_1 = 1678
gia_bac_2 = 1734
gia_bac_3 = 2014
moc_bac_1 = 100
moc_bac_2 = 200
tong_tien = 0
if kwh <= 0:
    tong_tien = 0
elif kwh <= moc_bac_1:
    tong_tien = kwh * gia_bac_1
elif kwh <= moc_bac_2:
    tien_bac_1 = 100 * gia_bac_1
    so_kwh_con_lai = kwh - 100
    tien_bac_2 = so_kwh_con_lai * gia_bac_2
    tong_tien = tien_bac_1 + tien_bac_2
else:
    tien_bac_1 = 100 * gia_bac_1
    tien_bac_2 = 100 * gia_bac_2
    so_kwh_con_lai = kwh - 200 
    tien_bac_3 = so_kwh_con_lai * gia_bac_3
    tong_tien = tien_bac_1 + tien_bac_2 + tien_bac_3
print(f"Tổng số tiền điện phải trả là: {tong_tien:.0f} VNĐ")