def rep_char(ch,n):
    for i in range(n):
        print(ch,end="")

name = input("Input his/her name:")

str1 = "Hello "+name+","
str2 = "Welcom to Seoul."

str_length = len(str1) if (len(str1)>len(str2)) else len(str2)

rep_char('-',str_length)
print()
print(str1)
print(str2)
rep_char("-",str_length)
