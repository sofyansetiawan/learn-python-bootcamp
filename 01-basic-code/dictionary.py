dict = { 'id': 1, 'name': "Sofyan", 'age': 30, 'address': 'Jakarta' }
print(dict["name"]) # akses key value

dict["name"] = 'Setiawan' # ubah key value
dict["age"] = 40

print(len(dict))

dict["gender"] = "male" #nambah key

# dict.pop("gender") #hapus key
dict.popitem() #hapus key terakhir
x = "save water"
print(x[3:8])
print(dict)