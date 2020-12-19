import datetime

x = datetime.datetime.now()

print(x) # date present tanggal dan jam second dari system computer

print(x.year) # cetak tahun saat ini

print(x.month) # cetak bulan saat ini

a = datetime.datetime(2020, 6, 4)
print(a)
print(a.month)

print(x.strftime("%B")) # string dari nama month
print(x.strftime("%A")) # string dari nama hari
print(x.strftime("%a")) # string dari nama hari (singkat)

