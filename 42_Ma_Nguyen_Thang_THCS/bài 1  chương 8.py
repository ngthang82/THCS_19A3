import math
def check_perfect_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    sqrt_n = math.sqrt(n)   
    return sqrt_n == int(sqrt_n)
if __name__ == "__main__":
    while True:
        try:
            number_str = input("Nhập một số nguyên dương để kiểm tra: ")
            if number_str.lower() == 'exit':
                print("Chương trình kết thúc.")
                break   
            number = int(number_str)           
            if number < 0:
                print(" Vui lòng nhập một số **nguyên không âm** (>= 0).")
                continue
            if check_perfect_square(number):
                root = int(math.sqrt(number))
                print(f" Số {number} là số chính phương vì {number} = {root} * {root}.")
            else:
                print(f" Số {number} không phải là số chính phương.")
        except ValueError:
            print(" Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")