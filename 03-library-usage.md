### Date

- module -> kelompok file atau satuan file external yang mempunyai sebuah define variabel, class, function dan sebagainya yang beberapa fungsional/fitur bisa kita manfaatkan ke file lain

- Cara memanfaatkan module dengan **import**

  ```python
  import loop.py
  ```

- Import module date (built-in module) -> `import datetime`

  ```python
  import datetime
  
  x = datetime.datetime.now()
  
  print(x) # date present tanggal dan jam second dari system computer
  ```

- Mendapatkan tahun saat ini -> `x.year`, bulan ini -> `x.month`dan masih banyak properti lainnya

- Membuat instance date dengan value sendiri

  ```
  a = datetime.datetime(2020, 06, 04) # yyyy, mm, dd jam menit detik jadi 0
  print(a)
  print(a.month)
  ```

- Date formating method -> Mendapatkan format manusiawi (User-friendly untuk user) bukan raw date data

  - https://stackabuse.com/how-to-format-dates-in-python/

    ```python
    print(x.strftime("%B")) # string dari nama month
    print(x.strftime("%A")) # string dari nama hari
    print(x.strftime("%a")) # string dari nama hari (singkat)
    ```



### File handling

- File handling -> manajemen file, directory di python (seperti fs di javascript)

  - Misal untuk menbaca file, upload file, upload gambar, akses directory

- Membuka File/Membaca File

  - Ketika membaca file -> menggunakan `open()` berisi path file (bukan nama file, pastikan di directory sama atau bukan, ekstensi file juga)

  - `"./namafile"` -> setara level directory, `"../namafile"` -> di parent level directory

  - Jika berada di child directory/level directory dibawah -> (akses dulu directory baru nama filenya) -> `"./directory/namafile"`

  - mode open file default adalah read ("r")

    ```python
    file = open("./test.txt", "r") # akses di directory/level directory yang sama, menyimpan setting path dan mode
    x = file.read() # membaca file dalam bentuk string
    
    print(x)
    ```

  - Jika file tidak ditemukan (salah panggil nama file, salah directory) -> error `FileNotFoundError`

- Membuat File

  - ```
    file = open("./test.txt", "w")
    file.write("Konten File.. \nIni adalah konten") # mengisi file dengan string
    file.close()
    ```

    - Menggunakan mode `w` untuk write file. `r` untuk read

    - close() -> untuk menutup file ketika mengisi data. Seperti save secara fungsi -> mengakhiri

    - Jika menjalankan lagi maka -> override file tersebut

    - Untuk memisahkan antar barus (seperti `<enter>`) maka gunakan -> `\n`

    - `write()`bisa dijalankan berkali kali misal dalam loop

      ```python
      str = ["By", "Sofyan", "Setiawan"]
      for item in str:
          file.write("\n" + item)
      file.close()
      ```

    - Gunakan encoding supaya aman mengenai jenis karakter -> `file = open("./test.txt", "r", encoding="utf-8")`

