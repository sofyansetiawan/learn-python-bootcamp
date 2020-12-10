name1 = "sofyan setiawan skom"
name2 = "HELLO WORLD"
print(name1)
# print(dir("array"))
print(name1.title())
print(name2.lower())

print(name1[0]) # s
print(len(name1)) # menghitung jumlah karakater / length

print(name1[len(name1) - 1]) # mencari karakter terakhir

name3 = name1.replace("s", "l") # melakukan replace karaketer

name4 = name2[0:5] # mengambil sebagian / split
name5 = name2[6:11] # mengambil sebagian / split
name6 = name2[-1] # mendapatkan huruf terakhir
name7 = name2[-2] # mendapatkan huruf terakhir kedua
name8 = name2[-3:-1] # mendapatkan rl
name9 = name2[:6] # mendapatkan slice dari 0, maka tidak perlu ditulis

name9

print(name3)
print(name4)
print(name5)
print("Huruf terakhir: ", name6)
print("Huruf terakhir ke-2: ", name7)
print("Slice rl: ", name8)
print("Slice dari 0-6:", name9)

a = "my"
b = "name"
c = "is"
d = a + " " + b + " " + c
e = "Sofyan"
ee = input()
ef = input()
f = "Hello {} {}".format(ee, ef)
g = "My Name is {1} {0}".format("Setiawan", "Sofyan")
print(f)
print(g)