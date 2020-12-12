### Function dan Method

- **Input**

  - User bisa input sesuai (nilai dari variabel belum pasti)

  - Gunakan input untuk memasukkan value dari user, terminal akan menunggu sampai user memasukkan value lalu `<enter>`

  - Hasil dari `input()` -> **String** 

  - Untuk perhitungan casting dulu dari `input()` ke integer

  - Defaultnya antar {} diurutkan. Kalau dibuat urutan gak default gunakan angka -> `{0} {1} {2}` (lebih kecil diurutkan seperti di array)

    ```python
    ee = input()
    ef = input()
    f = "Hello {} {}".format(ee, ef)
    g = "My Name is {1} {0}".format("Setiawan", "Sofyan")
    ```

  - Mau seperti template literal di JS, gunakan `f` sebelum quote string `""` -> `f"my name is {firstname} {lastname}"`

  

- **Function**

  - Function -> Sesuai yang melakukan tugas spesifik berupa block of code

  - Function -> Cara organisir kode

  - Function dapat digunakan berkali kali -> calling

  - Function -> menghindari repetitif, redundant process

  - Functon -> Lebih mudah di trace, modular dan maintainable

  - Function -> di python tidak ada pembukan dan penutup {} -> tergantung blok kode

  - Membuat function -> 

  - ````python
    def namafunction(param1, param2): #param1=1, param2=4
    	z = x + y
      return z
    
    namafunction(1, 4) # 5
    ````

  - Keyword `def` -> namafunction -> parameter (bisa lebih dari 1, untuk mewakili/melabeli dan sebagai jalan masuk value dari passing value argument ketika di invoke)

  - Kode di dalam blok function -> indentasi 1

  - Function terdiri dari -> input (paramater), process (kode di dalam function), output (return)

  - return -> output dari function sebagai value untuk variabel, output, argument function lain, dsb

  - Argument harus diisi sesuai parameter. Kalau tidak diisi sesuai parameter -> `ERROR` missing required positional argument: 'y'

  - Default Value diberikan jika argument tidak diisi -> pakai default value, jika diisi -> pakai value di argument

  - Default value -> mencegah error required params

    - `def namafunction(param1 = 0, param2 = 0):`

- **Errors**

  - Referensi -> Googling: Type errors in python

  - Syntax Error

    - Kesalahan syntax yang kurang lengkap (penulisan) sesuai ketentuan python
    - `a = 3 +` , `a 3` , `print(` -> SyntaxError: invalid syntax atau lainnya
    - Biasa langsung terdeteksi oleh editor misal -> vscode (tanpa merah zigzag)
    - Error ini menunjukkan di line -> `, line 39` dan arrow/token yang menunjukkan karakter mana yang kurang

  - Indentation Error

    - Ketika menulis global variabel dengan indentasi -> tanpa indentasi adalah global

    - Indentasi -> lingkup/scope kode yang seharusnya tergantung dia masuk ke scope apa (loop, condition, function)

    - Indentasi -> scope tergantung simbol `:` (setelah baris simbol `:` harus di tab)

    - Indentasi -> perbedaan tab

    - Misalnya ->

    - ```python
      def funct1(first, last):
      full = first + " " + last # indentasi karena dia ada blok function, bukan global
          return print(full)
      
      if("a" == "a"):
      print("Sesuai") # print harusnya di dalam
      ```

    - Python jangan di compress -> Karena indentasi

    - Jika variabel `a` di define di scope function dan dipanggil di global maka error undefined

  - Type Error

    - Melakukan pekerjaan / operasi yang tidak didukung oleh type data tertentu / type data berbeda

    - Misalnya: `x = 2 + "d"`

      ```python
      a = input("masukkan angka 1: ")
      b = input("masukkan angka 2: ")
      c = (a + b) + 2 # harus diubah ke int()
      print(c)
      ```

  - Name Error

    - Kalau kita mengakses atau memanggil variabel, function, class ->

      - tidak ada di program kita
      - tidak terdefinisi
      - tidak di scope tersebut
      - salah panggil nama (typo)

    - Variabel -> `print(x)`, padahal x tidak ada

    - Function -> 

      ```python
      def function1(a): 
          print(a)
      
      functio(100) # NameError
      ```

  - Zero Division Error

  - Index Error

  - Runtime Error

  - Attribute Error