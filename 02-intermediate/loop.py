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

