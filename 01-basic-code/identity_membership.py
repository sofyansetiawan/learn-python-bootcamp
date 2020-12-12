x = 4
y = 4
z = 10

print(x is y) # tipe data dan value sama
print(x is not y) # False
print(x is not z)

a = [1,2,3,4,5]
s = "Hello World"

b = 2
c = 20

print(b in a) # True value b adalah salah satu value dari list a
print(c not in a)
# print (c not in b) # Membandingkan bukan list / string . TypeError: argument of type 'int' is not iterable
# print(a in s) # TypeError: 'in <string>' requires string as left operand, not list
# print(b not in s) # TypeError: 'in <string>' requires string as left operand, not int
print(str(b) in s)
print((3 + 5 ** 2 - 2)*2)