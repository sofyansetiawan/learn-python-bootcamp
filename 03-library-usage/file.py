file = open("./test.txt", "r", encoding="utf-8") # akses di directory/level directory yang sama, menyimpan setting path dan mode
x = file.read() # membaca file dalam bentuk string

print(x)

# file = open("./tes.txt", "r") # error file not found

file = open("./test1.txt", "w")
file.write("Konten File..\nIni adalah konten") # mengisi file dengan string

str = ["By", "Sofyan", "Setiawan"]
for item in str:
    file.write("\n" + item)
file.close()

