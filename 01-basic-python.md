# Basic Python

- Install python3
- Buka terminal
- `print("Hello")`
- 3+3
- `exit()` -> untuk melakukan perintah exit
- touch first.py
  - `print("hello")`
- Hati hari dengan indentation error yang menunjukkan harusnya di blok tertentu kalau tidak ada blok mana di global, jangan ada indentasi
- Penulisan -> Penulisan kode harus dalam proper line. Python bukan free form language



### Coba Jupyter Notebook

- Buka website jupyter notebook

- Try in your browser

- Pilih python

- Akan keluar notebook yang tanpa file jadi dicompile disana (tanpa file dan install python), run directly

- Pilih File -> New Notebook -> Pilih Python 3

- Akan keluar editing environment -> Muncul 1 cell

- Pastikan dibagian dropdown tengah adalah Code

- Coba masukkan perintah pyton misal `3 + 4` atau `print('hello')`

- Menjalankannya dengan `SHIFT + ENTER` bukan `ENTER` -> keluar outputnya (seperti di console)

- Jika ingin menambahkan baris baru gunakan `enter`

- Simpan hasilnya ke File -> Download -> Notebook (.ipynb)

- Cara lain kalau mau menjalankan Jupyter di Local (Laptop)

- ```markdown
  # You can also get this tutorial and run it on your laptop:
  git clone https://github.com/ipython/ipython-in-depth
  Install IPython and Jupyter:
  
  with conda:
  
  conda install ipython jupyter
  
  with pip:
  # first, always upgrade pip!
  pip install --upgrade pip
  pip install --upgrade ipython jupyter
  
  Start the notebook in the tutorial directory:
  cd ipython-in-depth
  jupyter notebook
  ```



### Anaconda

- Jika tidak mau menjalankan jupyter notebook di browser pakai Anaconda (ada yang lain Zambia)
- Download Anaconda -> Versi Individual (Pastikan sudah install python 3)
- Buka Anaconda -> Jupyter Notebook
- Pilih New -> Python 3 atau Upload (file yang sudah ada)
- Coba ubah Untitled -> Coba Jupyper Local
- Jika membuat keterangan mengenai code kamu bisa pakai `markdown`



### Tipe Data

- Variabel -> Container data (Store Data)

- Variabel -> Menyimpan data di memory di alamat tertentu dengan dilabeli nama variabel yang bisa diakses bahasa pemrograman

- Variabel -> 2 jenis : `constant` (tidak bisa diubah nilainya tapi bisa dibaca) dan `non-constant`

- Ketika mau print di baca lain biasanya require dulu misal #include di C. Tapi di python tidak perlu

- Ketika type di python >>> variabel -> maka langsung output nilainya

- Untuk mendapatkan type data dari variabel atau value gunakan `type(namavariabel)` -> langsung output di terminal misal: `<class 'int'>`, `<class 'str'>`

- Tipe data number bisa melakukan operasi matematika

- Di python, float tetap tipe data number

- `type(8/3)` akan menghasilkan `<class 'float'>`

  

### Operasi di Number

- Operator Aritmatika -> + - * 3, ada power operator ** (seperti Math.pow())
- Parenthesis () -> menunjukkan operasi mana yang akan di consider menjadi expression pertama / prioritas didahulukan
- Operator punya higher desendent dibanding lainnya. Prioritasnya adalah () -> ** -> * / -> + -
- Bracket dibutuhkan selama bagian operator depan lebih rendah prioritas (lower-precedence) dibanding operator belakangnya
- Precedence itu -> left to right
- Ketika ada float number maka hasil perhitungan selalu mengubah hasil dari integer ke float
- Pembuatan .5 atas akan menghasilkan angka setelahnya misal 3.5 -> 4, 3.2 -> 3



### Dynamic Typing

- Di python dan javascript -> menerapkan dynamic typing. Di java, C#, C -> static typing

- Seperti di javascript, tidak perlu menentukan tipe data variable (dynamic typing). Tipe data variabel bisa diubah jenisnya tergantung assign value tipenya apa

  ```python
  a = "A";
  a = 13
  print(a)
  ```

- Penulisan variabel di python bisa pakai -> A-Z a-z 0-9 _ . Jangan pakai symbol lain
- Penulisan di python -> snake_case (readable) tapi camelCase juga bisa



### Casting

- Mengubah bentuk tipe data ke tipe data lain. Misal dari string ke number, float ke number

  ```python
  a = 10;
  b = str(a);
  c = 2.0;
  d = int(c);
  e = int("sofyan");
  ```



### String & Method

- Function dan method (dalam hal istilah..umumnya)

  - Built-in Function -> block code-code as function tapi terikat ke tipe data tertentu yang dikenali python dan function itu sudah tersedia di environment python
  - Method -> block code-code as function tapi terikat ke tipe data object atau instance dari class diluar environment python 

- Melihat built-in function bawaan tipe data tertentu gunakan `dir('string')` -> tipe data string (diterminal)

- Membuat huruf pertama dari string Capital -> `x.title()` (tidak modify nilai dari string, hanya reference)

- Membuat huruf menjadi huruf kecil semua -> `x.lower()`

  

- Mendapatkan item di string misal 1 huruf -> `x[2]` (dimulai dari 0)

- Slice (mengambil sebagian huruf) -> `x[1:5]` -> start, end

  - Untuk mendapatkan karakater terakhir -> `name1[len(name1) *-* 1])` atau `name1[-1]`
  - Untuk terakhir ke-2 -> `name1[-2]`. 
  - Trik lainnya slice bisa menggunakan `name1[-3:-1]`

- Slice dari index 0, maka tidak perlu ditulis angka pertamanya misal -> `name9 = name2[:6]`



- String Formating dengan Concatination -> +

- Jika ingin menggunakan format yang lebih mudah seperti Template Literal di JS -> `"text1 {} text2 {}".format(var1, var2)`

  ```python
  a = "my"
  b = "name"
  c = "is"
  d = a + " " + b + " " + c
  e = "Sofyan"
  f = "Hello {} {}".format(d, e)
  ```

- User bisa input sesuai (nilai dari variabel belum pasti) gunakan `.format()` (dynamis) dibanding concat (statis)

- Gunakan input untuk memasukkan value dari user, terminal akan menunggu sampai user memasukkan value lalu `<enter>`

- Defaultnya antar {} diurutkan. Kalau dibuat urutan gak default gunakan angka -> `{0} {1} {2}` (lebih kecil diurutkan seperti di array)

  ```python
  ee = input()
  ef = input()
  f = "Hello {} {}".format(ee, ef)
  g = "My Name is {1} {0}".format("Setiawan", "Sofyan")
  ```

- Mau seperti template literal di JS, gunakan `f` sebelum quote string `""` -> `f"my name is {firstname} {lastname}"`



### List

- List -> seperti array -> collection of datatype value (item)
- Type collection di python -> list, set, dictionary, tuple
- List -> value-value di dalam `[]` (Pemisah value adalah comma `,`)
- Akses index nya -> mirip string
- Mendapatkan jumlah item di dalam list -> `len(list1)`
- Menghapus (sambil mendapatkan) item terakhir di list -> `x.pop()`
- Menambahkan item terakhir di list -> `x.append("Sofyan")`
- Menghapus 1 (awal ditemukan) dengan value tertentu -> `x.remove("jakarta")`
- Menghapus variabel list -> `del(x)` (kalau masih dipanggil akan error) -> NameError: name 'x' is not defined



### Tuple

- Tuple -> seperti list yang membedakan -> element dalam tuple tidak bisa diganti / konstanta
- Tuple -> tidak bisa dimanipulasi (pop, append, assign item)
- Tuple -> value value di dalam `()` / **parenthesis** (pemisah antar value dalam comma ,)
- Akses index seperti -> list, string -> `tuple1[2]`
- Tuple -> tidak punya built-in function untuk modifikasi pop, append, dsb
- Tuple -> Biasanya cuma digunakan sebagai dictionary list
- Cek perintah di tuple -> `dir(tuple)`



### Dictionary

- Dictionary -> seperti object -> element dalam dictionary harus dalam key dan value -> bukan by index
- Misalkan -> `{ "id": 1, "name": "Sofyan", "age": 30 }`
- Penulisan key di dictionary -> di dalam single-quote atau double-quote
- Akses element di dictionary -> `dict["name"]` -> bracket berisi key. Tidak bisa pakai dot `.` seperti di JS
- Change Value di key -> `dict["name"] *=* 'Setiawan'`
- Banyak ite di dictionary -> `len(dict)`
- Add key value -> `dict["gender"] = "male"` -> pastikan nama key tidak sama, jika sama diubah, jika tidak sama di tambahkan
- Hapus item (mendapatkan)-> `dict.pop("gender")`
- Hapus item terakhir (mendapatkan) -> 



### Boolean

- Boolean -> 2 value -> **True** atau **False**
- Boolean juga dihasilkan dari operator logic & comparison dari 2 nilai -> 2 > 3, "sofyan" === "setiawan", 10 >= x, "10" === 10
- Boolean bisa disimpan di variabel -> `x = True`



### Operator

- 7 type operator:
  - Arithmetic
  - Assignment
  - Comparison
  - Logical
  - Identity (less usage)
  - Membership
  - Bitwise (less usage)

- Arithmetic (Kalkulasi Matematik)
  - `+` (addition) -> untuk number atau concat string
  - `-` (substract)
  - `*` (multiply)
  - `/` (floating-point division)
  - `//`(floor integer division)
    - Pembulatan kebawah `9 // 2` -> 4, bukan 4.5
  - `%` (remainder)
    - Ada left portion
  - `**` (double-star -> pow / pangkat)
- Assignment
  - 