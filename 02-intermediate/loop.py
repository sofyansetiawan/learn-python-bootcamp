# FOR-IN
# ------

list1 = [1,2,3,4,5,6,7,8,9]

list2 = ["Blue", "Red", "Green", "Yellow"]

for item in list1: # item -> element di list
    print(item) # mencetak item setiap item berurutan

# seperti
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)

for element in list2: # item -> element di list
    print(element) # mencetak item setiap item berurutan

for i in list1:
    list1[i-1] = input("Replace Character with: ") # i adalah item, bukan index. Kasus seperti ini gunakan ranged()
print(list1)

# While
# ---------

i = 0 # initial condition
while i < 6:
    print(i) # jika counter tidak dihentikan maka akan infinity loop
    i+=1

# BREAK
# -----------

listColor = ["A", "B", "C", "D", "E", "F"]

for item in listColor:
    if item == "C":
        break; # ketika C maka berhenti tidak menjalankan iterasi berikutnya
    print(item)

for item in listColor:
    if item == "C":
        continue; # ketika C akan di skip lanjut ke element list berikutnya
    print(item)

# Range Function
# ------------

for x in range(4): # start 0, stop 4, step 1
    print(x)

for x in range(4, 10): # start 4, stop 10, step 1
    print(x)

for x in range(10, 200, 10): # start 0, stop 200, step 10
    print(x)

a = 100

while(a < 200):
    print(a)
    a += 10
else:
    print("Apa ini")

# Nested Loop
# ------------

n = ["big", "small", "bold", "light", "heavy"]

m = ["iron", "silver", "gold", "platinum", "diamond"]

for size in n:
    for matter in m:
        print(size, matter) # item list1 pertama, item list2 pertama....n ->  item list1 kedua, item list2 pertama...n, item list1 ketiga, item list2 pertama...n

a = 0
b = 0
for size in n: # iterasi luar tidak lanjut kalau iterasi dalam belum selesai
    for matter in m: #iterasi inner loop berjalan awal sampai akhir di 1 step iterasi luar
        print(n[a], m[b]) # akses by index
        b += 1 # akses index 1 step
    a += 1 # akses index 1 step untuk iterasi luar
    b = 0 # reset ketika sudah selesai iterasi dalam supata tidak tertambah terus kalai lanjut iterasi luar bisa IndexError. Element 5 tapi iterasi luar 0 -> 0,1,2,3,4 -> iterasi luar 1 -> 5,6,7,8,9 harusnya balik jadi 0