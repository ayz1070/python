rate = int(input("할인율은? "))

def get_discount_price(product):
    return int(input("%s 상품의 할인된 가격은? " %product))
       
def get_fixed_price(discount,rate):
    return int(discount / (1-rate/100))

discount_A = get_discount_price("A")
discount_B = get_discount_price("B")

print("A 상품의 정가는 ",get_fixed_price(discount_A,rate))
print("B 상품의 정가는 ",get_fixed_price(discount_B,rate))



