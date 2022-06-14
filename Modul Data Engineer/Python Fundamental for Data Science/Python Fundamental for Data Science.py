
#Modul 1 Data Engineer

# # Code Hello World

print(10*2+5)
print("AcademyDQLab")

# # Memberikan comment pada Python

print(10*2+5) #fungsi matematika
print("Academy DQLab") #fungsi menctak kalimat

# # Memperlihatkan tipe-tipe data yang ada pada Python

var_string = "Belajar Python DQLAB"
var_int = 10
var_float = 3.14
var_list = [1, 2, 3, 4]
var_tuple = ("satu", "dua", "tiga")
var_dict = {"nama": "Ali", "umur": 20}

print(var_string)
print(var_int)
print(var_float)
print(var_list)
print(var_tuple)
print(var_dict)

print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))


# # Memperkenalkan IF Statement pada Python

i = 7 # memberikan variable i dengan nilai 7

if(i == 10): # pengecekan nilai i apakah sama dengan 10
	print("ini adalah angka 10") # menampilkan kata berikut jika pengecekan bernilai benar
  
# # Memperkenalkan IF ELSE pada Python

i = 5 

if(i==10):
	print("ini adalah angka 10")  # menampilkan kata berikut jika pengecekan bernilai benar
else:
	print("bukan angka 10") # menampilkan kata berikut jika pengecekan bernilai salah
  
# # Memperkenalkan IF ELIF dan ELSE pada Python

i = 3 

if(i==5):
	print("ini adalah angka 5") # menampilkan kata berikut jika pengecekan i == 5 benar
elif(i>5):
	print("lebih besar dari 5") # menampilkan kata berikut jika pengecekan i > 5 benar
else:
	print("lebih kecil dari 5") # menampilkan kata berikut jika semua pengecekan bernilai salah
  
# # Memperkenalkan IF di dalam IF

i = 2 
if(i<7): 
	print("nilai i kurang dari 7") 
	if(i<3): 
		print("nilai i kurang dari 7 dan kurang dari 3") 
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")
    
# # Praktik Operasi Matematika

a = 10
b = 5
selisih = a-b
jumlah = a+b
kali = a*b
bagi = a/b
print("Hasil penjumlahan a dan b adalah ", jumlah)
print("Selisih a dan b adalah :", selisih)
print("Hasil perkalian a dan b adalah :", kali)
print("Hasil pembagian a dan b adalah:", bagi)

# # Operasi Modulus (Sisa Pembagian)

c = 10
d = 3
modulus = c%d
print("Hasil modulus ", modulus)

# # Tugas Mid Praktek
# # 1. Buat variabel dengan nama “angka” yang diisi dengan nilai 10
# # 2. Menentukan variablel angka modulus 2 bernilai 0.
