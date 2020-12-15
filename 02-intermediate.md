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

    - Ketika kita melakukan pembagian dengan 0 -> karena akan menghasilkan **Infinity**
    - `x = 4 / 0`
    - Hanya berlaku jika sebuah type data integer/number

  - Index Error

    - Ketika mengakses index:

      - tidak ditemukan di array
      - bukan type data number
      - menghasilkan angka float
      - dibawah 0 atau melebihi index terakhir array

      ```python
      word = "Hello World"
      print(word[22]) # tidak ada index 22 karena index terakhir adalah 10
      print(word[len(word)-1]) # bisa
      print(word[-1]) # bisa
      print(word[-30])
      ```

  - Attribute Error

    - Error ini terjadi kalau menggunakan built-in function yang tidak tersedia di type data tersebut

    - Misalkan menggunakan built string tapi untuk type data int

      ```python
      x = 40
      x.title()
      ```

  - Runtime Error

    - Error yang lain tidak ditangkap oleh yang lain. Biasanya terjadi kesalahan logic program

- **Condition**

  - Menggunakan `if` -> Jika kriteria menghasilkan True maka flow akan masuk ke blok kode if. Jika tidak maka tidak dijalankan

  - Karena menggunakan blok kode selalu pakai symbol `:` dan indentasi tab -> isi kodenya

    ```python
    x = 3
    y = 3
    if(x == y):
        print("they are equals")
    if(x != y):
        print("the are not equals")
    
    print("program is working fine")
    ```

  - Jika flow tidak masuk ke True, maka akan menjalankan baris berikutnya diluar blok If. Jika ingin dihandle bagian False maka gunakan `else`

    ```python
    x = 3
    y = 3
    if(x == y):
        print("they are equals")
    else:
        print("the are not equals")
    
    print("program is working fine")
    ```

  - Jika ada kriteria yang lain selain `if`, gunakan `elif`.

  - `elif `-> bisa lebih dari 1 dan ketika tidak masuk ke `elif` pertama bisa masuk ke `elif` berikutnya

  - Biasanya ada analogi -> tombol button quiz A, B, C, D atau remote control

    ```python
    a = 10
    b = 10
    c = 80
    
    if(a == b):
        print("a is equals b")
    elif(b > a):
        print("b is greater than a")
    elif(a > b):
        print("a is greater than b")
    else:
        print("the are not equals")
    ```

  - Urutannya adalah if -> elif -> else

  - Kamu bisa gunakan operator di dalam condition

    - Comparison
    - Logical

    ```python
    skor = 80
    
    if(skor >= 80 and skor <= 100):
        print("Nilai Kamu A")
    elif(skor >= 60 and skor < 80):
        print("Nilai Kamu B")
    elif(skor >= 40 and skor < 60):
        print("Nilai Kamu C")
    elif(skor >= 0 and skor < 40):
        print("Nilai Kamu D")
    else:
        print("Nilai kamu tidak valid")
    ```

  - Kamu bisa buatkan `nested condition` -> condition di dalam condition

    - Jika flow program masuk ke dalam blok condition maka akan diperiksa lagi ke condition apakah masuk ke blok condition berikutnya
    - Nested condition -> dimulai dari if, tidak bisa langsung elif atau else

- **Loops**

  - Loops -> Proses flow yang masuk condition yang dijalankan berulang ulang

  - Loop ada jenisnya -> `for`, `while` 

    - Step -> `in` (untuk list, dictionary) , `ranged()` (untuk angka)

  - Umumnya loop dibutuhkan ketika:

    - Melakukan output berulang ulang berdasarkan input
    - Memanggil semua item list satu persatu
    - Mencari karaketer di string satu persatu
    - Melakukan perhitungan untuk mengisi nilai secara increment

  - Untuk `for-in` (list)

    ```python
    list1 = [1,2,3,4,5,6,7,8,9]
    
    for item in list1: # item -> value element di list
        print(item) # mencetak item setiap item berurutan
    ```

    - item -> menamai / melabeli setiap element/item di dalam list / dictionary (bukan Indexnya)
    - For-in untuk list defaultnya adalah iterasi dari element pertama sampai element akhir dengan step 1 per satu

  - Untuk `while`

    - While umumnya dipakai kalau kita tidak tahu limit berapa kali sampai ada trigger untuk berhenti

    - Biasanya tetap pakai start (initial condition, step (increment/decrement) dan finished (target/limit di condition)

      ```python
      i = 0 # initial condition
      while i < 6:
          print(i) # jika counter tidak dihentikan maka akan infinity loop
          i+=1
      ```

    - Jika tidak ada step maka terjadi infinite loop (hentikan CTRL+C)

    - While digunakan biasanya bukan untuk kasus list -> kondisi angka atau flagging (toggle) boolean

  - Break

    - Digunakan untuk exit condition dari loop di scope tersebut ketika sudah menyentuh iterasi ketika flow masuk kondisi break

      ```python
      listColor = ["A", "B", "C", "D"]
      
      for item in listColor:
          if item == "C":
              break; # ketika C maka berhenti tidak menjalankan iterasi berikutnya
          print(item)
      ```

    - Break tidak akan menjalankan kode dibawahnya di dalam scope loop. Contohnya: tidak menjalankan print setelah break 

  - Continue

    - Digunakan untuk melakukan skip 1 step dari loop tapi tidak exit condition. Contohnya kalau loop list -> item tersebut di skip

      ```
      for item in listColor:
          if item == "C":
              continue; # ketika C akan di skip lanjut ke element list berikutnya
          print(item)
      ```

    - Continue tidak akan menjalankan kode dibawahnya di dalam scope loop. Contohnya: tidak menjalankan print setelah continue

  - Range Function

    - Range -> Untuk melakukan looping dalam ranged angka (tanpa terikat tipe data list)

    - Range terdiri dari argument -> start, stop dan step

    - Default dari range adalah start < stop (kurang dari)

    - Kalau diisi 1 argument -> stop. Dimulai dari 0 sampai angka stop, step 1 per satu. Misalkan `*for* x *in* range(4):` -> `0,1,2,3`

    - Kalau diisi 2 argument -> start, stop. Dimulai dari angka start sampai angka stop, stepnya 1 per satu. Misalkan `*for* x *in* range(4, 10):` -> `4,5,6,7,8,9,`

    - Kalau diisi 3 argument -> start, stop, step. Dimulai dari angka start sampai angka stop, stepnya tergantung angka step. Misalkan `*for* x *in* range(10, 200, 10):` -> `10, 20, 30, ... 170, 180, 190` (200 tidak ikut )

      ```python
      for x in range(4): # start 0, stop 4, step 1
          print(x)
      
      for x in range(4, 10): # start 4, stop 10, step 1
          print(x)
      
      for x in range(10, 200, 10): # start 0, stop 200, step 10
          print(x)
      ```

  - Else di Loop

    - Else di loop dijalankan kalau kondisi dari loop tidak terpenuhi atau ketika condition sudah selesai

    - Sebenarnya else dalam loop tidak diperlukan

      ```python
      a = 100
      
      while(a < 200):
          print(a)
          a += 10
      else:
          print("Apa ini")
      ```

  - Nested Loop

    - Nested loop digunakan umumnya ketika melakukan iterasi sampai selesai di sebuah step iterasi lain

    - Umumnya kalau membuat pola atau memasangkan item list 1 dengan lainnya

    - Jika ada for-in dalam for-in -> di iterasi pertama dari outerloop, inner loop akan melakukan iterasi dari awal sampai akhir sebanyak n sampai selesai. Setelah itu baru outerloop akan melakukan iterasi kedua, inner loop akan melakukan iterasi dari awal sampai akhir sebanyak n sampai selesai.. seterusnya sampai outer loop selesai

      ```python
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
      ```

    - Iterasi luar tidak lanjut kalau iterasi dalam belum selesai

    - Iterasi inner loop berjalan awal sampai akhir di masing masing step iterasi luar

