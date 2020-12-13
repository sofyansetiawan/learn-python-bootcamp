x = 3
y = 3
if(x == y):
    print("they are equals")
else:
    print("the are not equals")

print("program is working fine")

# ------------------

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
    
# -------------------------

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

# --------------------------

types = "Human"
names = "Sofyan"
ages = 30

if(types == "Human"):
    if(ages >= 20):
        print(f"Welcome.Please {names} drink this beer")
    else:
        print(f"Welcome.Please {names} drink this juice")
else:
    print("You cant enter this house")