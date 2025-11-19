def find_gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numerator, denominator):
    if denominator == 0:
        return "Lỗi", "Mẫu số không được bằng 0"
    if numerator == 0:
        return 0, 1
    common_divisor = find_gcd(numerator, denominator)
    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor   
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den       
    return simplified_num, simplified_den
if __name__ == "__main__":
    while True:
        try:
            print("\n--- Rút Gọn Phân Số ---")           
            numerator_str = input("Nhập **Tử số** (hoặc 'exit'): ")
            if numerator_str.lower() == 'exit':
                print("Chương trình kết thúc.")
                break              
            numerator = int(numerator_str)           
            denominator_str = input("Nhập **Mẫu số**: ")
            denominator = int(denominator_str)            
            simplified_num, simplified_den = simplify_fraction(numerator, denominator)          
            if simplified_den == "Mẫu số không được bằng 0":
                print(f" Lỗi: {simplified_den}")
            elif simplified_den == 1:
                print(f" Phân số {numerator}/{denominator} rút gọn thành: **{simplified_num}**")
            else:
                print(f" Phân số {numerator}/{denominator} rút gọn thành: **{simplified_num}/{simplified_den}**")
        except ValueError:
            print(" Lỗi: Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")