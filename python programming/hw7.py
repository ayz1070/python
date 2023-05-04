shopping_bag={}
while True:
    item = input("상품명? ")
    if item == '':
        break
    count = int(input("수량은? "))
    
    shopping_bag[item]=count
    print(f"장바구니에 {item} {count}개가 담겼습니다.")

print(f"장바구니 보기: {shopping_bag}")
