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

