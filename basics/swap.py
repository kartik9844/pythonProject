a = int(input("enter a number a  "))
b = int(input("enter a number b  "))

# inter change
print("direct swap")
a, b = b, a
print(a)
print(b)

# inter change temp
print("temp way")
tem = a
a = b
b = tem
print(a)
print(b)

# inter change add
print("add method")
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# inter change
print("mul ")
a = a*b
b = a/b
a = a/b
print(a)
print(b)
