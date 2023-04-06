def read_single_digit(i):
    if i == '0':
        return "영"
    elif i == '1':
        return "일"
    elif i == '2':
        return "이"
    elif i == '3':
        return "삼"
    elif i == '4':
        return "사"
    elif i == '5':
        return "오"
    elif i == '6':
        return "육"
    elif i == '7':
        return "칠"
    elif i == '8':
        return "팔"
    elif i == '9':
        return "구"

def read_number():
    return input("세 자리 정수 입력:")

n = read_number()

s=""
for i in n:
    s += read_single_digit(i)+" "

print(s)
