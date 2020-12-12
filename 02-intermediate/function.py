a = 3
b = 5
c = a + b
print(c)

d = 5
e = 20
f = d + e
print(f)

g = 5
h = 9
i = g + h
print(i) # proses repetitif, tidak efisien

# tanpa perlu menulis nulis ulang seperti yang diatas

def add(param1, param2):
    z = param1 + param2
    print(z)

add(a, b) # proses kode sama dengan c
add(d, e)
add(g, h)

# return version ->

def add1(param1 = 0, param2 = 0): #default parameter
    z = param1 + param2
    return z

j = add1(a, b) # proses kode sama dengan c
print(j)
print(add1(d, e))
add(add1(g, h), 20)

# user input dan function

x = input("Masukkan angka pertama: ")
y = input("Masukkan angka kedua: ")
x = int(x)
y = int(y)

add(x, y)

def celtofahren(number):
    return ( 9 / 5 ) * number + 32

print(celtofahren(40))

def len(m, s):
    return int(m)/60 + int(s)/3600

print(len(60, 3600))

## Mencegah Error

def div(a, b):
    if(b == 0): # cara untuk control flow
        return print("this is not possible")
    else:
        c = a / b
        print(c)

div(int("4"), int("0"))