num=int(input("Enter a number:"))

res=lambda num:num%2+3
res2=lambda num:num+60
x = lambda a, b : a * b
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print(x(5, 6))
print(res(num))
print(res2(num))