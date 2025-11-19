def find_gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    while True:
        try:
            print("\n--- Tìm Ước Chung Lớn Nhất (GCD) ---")
            num1_str = input("Nhập số nguyên thứ nhất (a, hoặc 'exit'): ")
            if num1_str.lower() == 'exit':
                print("Chương trình kết thúc.")
                break
            num2_str = input("Nhập số nguyên thứ hai (b): ")
            num1 = int(num1_str)
            num2 = int(num2_str)  
            if num1 == 0 and num2 == 0:
                print(" Ước chung lớn nhất của 0 và 0 là không xác định (hoặc được coi là 0), nhưng thường chỉ xét cho ít nhất một số khác 0.")
                continue
            result = find_gcd(num1, num2)
            print(f" Ước chung lớn nhất (GCD) của {num1} và {num2} là: **{result}**")
        except ValueError:
            print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")