-- Mengambil Seluruh Kolom dalam suatu Tabel

select * from ms_produk;

-- Mengambil Satu Kolom dari Tabel

select nama_produk from ms_produk;

-- Mengambil Lebih dari Satu Kolom dari Tabel

select nama_produk,harga from ms_produk;

-- Membatasi Pengambilan Jumlah Row Data

select nama_produk, harga from ms_produk limit 5;

-- Penggunaan SELECT DISTINCT statement

select distinct nama_customer, alamat from ms_pelanggan;

-- Menggunakan Prefix pada Nama Kolom

select ms_produk.kode_produk from ms_produk;

-- Menggunakan Alias pada Kolom

select no_urut as nomor, nama_produk as nama from ms_produk;

-- Menghilangkan Keyword 'AS'

select no_urut nomor, nama_produk nama from ms_produk;

-- Menggabungkan Prefix dan Alias

select ms_produk.harga as harga_jual from ms_produk;

-- Menggunakan Alias pada Tabel

select * from ms_produk t2;

-- Prefix dengan Alias Tabel

select t2.nama_produk, t2.harga from ms_produk t2;

-- Menggunakan WHERE

select * from ms_produk where nama_produk = 'Tas Travel Organizer DQLab';

-- Menggunakan Operand OR

select * from ms_produk 
where nama_produk = 'Gantungan Kunci DQLab' 
OR nama_produk = 'Tas Travel Organizer DQLab' 
OR nama_produk = 'Flashdisk DQLab 64 GB';

-- Filter untuk Angka

select * from ms_produk where harga > 50000;

-- Menggunakan Operand AND

select * from ms_produk where nama_produk = 'Gantungan Kunci DQLab' 
AND harga < 50000;

-- Mini Project
-- Menyiapkan data transaksi penjualan dengan total revenue >= 100000

select kode_pelanggan, nama_produk, qty, harga, qty*harga as total 
from tr_penjualan 
where qty*harga>=100000 
order by total desc;
