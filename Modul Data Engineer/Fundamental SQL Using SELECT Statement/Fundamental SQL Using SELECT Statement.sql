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

--
