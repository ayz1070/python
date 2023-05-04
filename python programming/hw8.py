shopping_bag={}
while True:
    item = input("상품명? ")
    if item == '':
        break
    count = int(input("수량은? "))
    
    shopping_bag[item]=count
    print(f"장바구니에 {item} {count}개가 담겼습니다.")

print(f"장바구니 보기: {shopping_bag}")

search = input("장바구니에서 확인하고자 하는 상품은? ")
find = ''
for i in shopping_bag:
    if i == search:
        find = i
if find != '':
    print(f"{find}(는) {shopping_bag[find]}개 담겨있습니다.")
else:    
    print(f"장바구니에 {search}은(는) 없습니다.")
