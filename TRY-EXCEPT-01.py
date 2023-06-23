def soChia(biChia): #try except là để tránh crash chương trình do lỗi
    try:
        return 42 / biChia
    except ZeroDivisionError:
        print('Lỗi! Không chia được cho 0')

print(soChia(2))
print(soChia(22))
print(soChia(0)) #hàm luôn trả về giá trị nên ở đây xuất hiện None
print(soChia(12))