luong_co_ban = float(input("Nhập lương cơ bản: "))
so_ngay_cong = float(input("Nhập số ngày công trong tháng: "))
NGAY_CONG_CHUAN = 22
TI_LE_THUONG = 0.10 
TI_LE_PHAT = 0.05  
luong_mot_ngay = luong_co_ban / NGAY_CONG_CHUAN
luong_thuc_te = luong_mot_ngay * so_ngay_cong
tien_thuong = 0
tien_phat = 0
if so_ngay_cong > NGAY_CONG_CHUAN:
    tien_thuong = luong_thuc_te * TI_LE_THUONG
elif so_ngay_cong < NGAY_CONG_CHUAN:
    tien_phat = luong_thuc_te * TI_LE_PHAT
tong_luong_thuc_nhan = luong_thuc_te + tien_thuong - tien_phat
print(f"Tổng tiền lương thực nhận là: {tong_luong_thuc_nhan:.0f} VNĐ")