def get_radius():
    r = int(input())
    return r

def get_circle_area(r):
    return 3.14*r*r 

print("넓이를 구하고자 하는 원의 반지름은? ", end='')
radius = get_radius()
width = get_circle_area(radius)
print("반지름이 ",radius,"인 원의 넓이 = 3.14 x ",radius," x ",radius," = ", width)
