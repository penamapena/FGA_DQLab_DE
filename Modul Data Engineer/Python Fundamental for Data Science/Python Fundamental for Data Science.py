
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
# # 1. Buat variabel dengan nama “angka” yang diisi dengan nilai 10 yang kemudian diganti dengan 5
# # 2. Menentukan variablel angka termasuk bilangan genap atau ganjil

angka=5

if(angka%2 == 0):
    print("angka termasuk bilangan genap")
else:
    print("angka termasuk bilangan ganjil")

# # Fungsi While

j = 0
while j<6: # Ketika j masih kecil dari 6 maka proses akan berulang
	print("Ini adalah perulangan ke -", j)
	j=j+1

# # Fungsi For

for i in range(1,6): # untuk i pada range 1 sampai 6 (auto step 1) jika ingin menambah step (awal, akhir, step)
	print("Ini adalah perulangan ke -", i) 

# # Fungsi for tahap lanjut

for i in range (1,11):
    if(i%2 == 0):
        print("Angka genap",i)
    else:
         print("Angka ganjil",i)

# # Membuat Fungsi

def salam():
	print("Hello, Selamat Pagi")
	
salam() # memanggil fungsi salam

# # Fungsi dengan parameter

def luas_segitiga(alas, tinggi): # (alas, tinggi) merupakan parameter yang harus dimasukkan
	luas = (alas*tinggi)/2
	print("Luas segitiga: %f",luas);
	
luas_segitiga(4,6)

# # Fungsi dengan Return Value

def luas_segitiga(alas, tinggi):
	luas = (alas*tinggi)/2
	return luas

print("Luas segitiga: %d" %luas_segitiga(4,6))

# # Import Package dan Menggunakan modul

import math # salah satu library pada python
print("Nilai pi adalah:", math.pi)

# # Import dengan Module Rename atau Alias

import math as m
print("Nilai pi adalah:", m.pi)

# # Import Sebagian Fungsi

from math import pi
print("Nilai pi adalah", pi)

# # Import Semua isi Moduls

from math import *
print("Nilai e adalah:", e)

# # Membaca Teks File (CSV)

import requests
from contextlib import closing
import csv

url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

with closing(requests.get(url, stream=True)) as r:
	f = (line.decode('utf-8') for line in r.iter_lines())
	reader = csv.reader(f, delimiter = ',')


	for row in reader:
		print(row)

# # Membaca file CSV dengan menggunakan PANDAS

import pandas as pd

pd.set_option("display.max_columns", 50)

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)

# # Pengenalan Bar Chart

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.show()

# # Parameter dalam Grafik (Memberikan Nilai Axis dari data CSV)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)
plt.show()

# # Menambah Title dan Label pada Grafik

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Kelurahan di Jakarta Pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki - Laki di Jakarta Pusat')

plt.show()
