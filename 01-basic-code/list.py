x = ["Sofyan Setiawan", "jakarta1", "jakarta", "jakarta1", True, 30, 176.5]

print(x[0]) # akses item pertama

print(len(x)) # len di python bukan sebagai method built-in

dihapus = x.pop() # menghapus item terakhir di list
x.append("Ponorogo") # menghapus item terakhir di list
numItem = len(x) # length
x.remove("jakarta1") # menghapus 1 item jakarta (paling awal ditemukan)

print(dihapus)
print(x[-2]) ## akses item di list 2 dari belakang
print(x)
print(numItem)
del(x) # menghapus variabel list
print(x)