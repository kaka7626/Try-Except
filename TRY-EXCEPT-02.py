print('Bạn có bao nhiêu con mòe?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Nhiều mòe quá đấy!')
    elif int(numCats) < 0:
        print('Bạn không thể nhập số âm được :v')
    elif int(numCats) == 0:
        print('Không có con mòe nào à?')
    else:
        print('Ít mòe quá nhỉ?')

except ValueError:
    print('Bạn phải nhập số vào chứ -,-')
