
-- Tugas Awal

select * from ms_item_kategori;
select * from ms_item_warna;

-- Menggabungkan Tabel dengan Key Columns

select * from ms_item_kategori, ms_item_warna
where nama_barang = nama_item;

-- Bagaimana jika urutan Tabel diubah?

select * from ms_item_warna, ms_item_kategori
where nama_barang = nama_item;

-- Menggunakan Prefix Nama Tabel

select ms_item_kategori.*, ms_item_warna.*
from ms_item_warna, ms_item_kategori
where nama_barang = nama_item;

-- Penggabungan Tanpa Kondisi

select * from ms_item_kategori, ms_item_warna;

-- Tugas Praktek: Menggunakan INNER JOIN (1/3)

select * from ms_item_warna
inner join ms_item_kategori
on ms_item_warna.nama_barang = ms_item_kategori.nama_item;

-- tabel tr_penjualan dan tabel ms_produk

select * from tr_penjualan;
select * from ms_produk;

-- Tugas Praktek: Menggunakan INNER JOIN (2/3)

select * from tr_penjualan
inner join ms_produk
on tr_penjualan.kode_produk = ms_produk.kode_produk;

-- Tugas Praktek: Menggunakan INNER JOIN (3/3)

SELECT tr_penjualan.kode_transaksi, tr_penjualan.kode_pelanggan, tr_penjualan.kode_produk, 
ms_produk.nama_produk, ms_produk.harga,tr_penjualan.qty, ms_produk.harga*tr_penjualan.qty as total
FROM tr_penjualan
INNER JOIN ms_produk
ON tr_penjualan.kode_produk = ms_produk.kode_produk;

-- UNION (Tabel yang Akan Digabungkan)

select * from tabel_A;
select * from tabel_B;

-- Menggunakan UNION

select * from tabel_A
union
select * from tabel_B;

-- Menggunakan UNION dengan Klausa WHERE

select * from tabel_A
where kode_pelanggan = 'dqlabcust03'
union
select * from tabel_B
where kode_pelanggan = 'dqlabcust03';

-- Menggunakan UNION dan Menyelaraskan Kolom-Kolomnya.

select CustomerName, ContactName, City, PostalCode
from Customers
union
select SupplierName, ContactName, City, PostalCode
from Suppliers;

-- Project INNER JOIN

select distinct tr_penjualan.kode_pelanggan, ms_pelanggan.nama_customer, ms_pelanggan.alamat
from ms_pelanggan
inner join tr_penjualan
on tr_penjualan.kode_pelanggan = ms_pelanggan.kode_pelanggan
where tr_penjualan.nama_produk = 'Kotak Pensil DQLab' 
or tr_penjualan.nama_produk = 'Flashdisk DQLab 32 GB' 
or tr_penjualan.nama_produk = 'Sticky Notes DQLab 500 sheets';

-- Project UNION

select nama_produk, kode_produk, harga
from ms_produk_1
where harga < 100000
union
select nama_produk, kode_produk, harga
from ms_produk_2
where harga < 50000;
