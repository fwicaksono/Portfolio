# Supply Chain Optimization: TechMart Electronics

## Deskripsi Proyek
Proyek ini bertujuan untuk mengoptimalkan rantai pasok (supply chain) perusahaan **TechMart Electronics**, yang bergerak di bidang penjualan produk elektronik seperti laptop, smartphone, dan tablet. Dataset yang disediakan mencakup informasi tentang permintaan produk, inventaris, biaya pemasok, waktu pengiriman, dan biaya penyimpanan.

## Problem Statement
TechMart Electronics menghadapi beberapa masalah dalam manajemen rantai pasoknya, yaitu:
1. **Tingkat Inventaris Tidak Optimal:**  
   - Terkadang stok produk habis sebelum pesanan baru tiba (stockout), menyebabkan kehilangan penjualan.
   - Di sisi lain, ada juga kelebihan stok yang mengakibatkan biaya penyimpanan tinggi.

2. **Biaya Operasional Tinggi:**  
   - Biaya pemesanan dan penyimpanan yang tidak terkelola dengan baik menyebabkan margin keuntungan menurun.

3. **Ketidakpastian Permintaan:**  
   - Permintaan produk berfluktuasi setiap bulannya, sehingga sulit untuk merencanakan produksi dan pengadaan.

4. **Waktu Pengiriman yang Bervariasi:**  
   - Lead time dari pemasok bervariasi, sehingga sulit untuk memprediksi kapan stok akan tiba.

**Tujuan:**  
TechMart Electronics ingin mengoptimalkan rantai pasoknya dengan:
1. Menentukan **jumlah pesanan optimal** untuk setiap produk.
2. Meminimalkan **total biaya operasional** (biaya pemesanan + biaya penyimpanan).
3. Memastikan **ketersediaan stok** untuk memenuhi permintaan pelanggan.
4. Meningkatkan **efisiensi rantai pasok** secara keseluruhan.

## Dataset
Dataset ini terdiri dari **1000 baris** dan mencakup kolom-kolom berikut:

| **Kolom**         | **Deskripsi**                                                                 |
|--------------------|-------------------------------------------------------------------------------|
| **Product_ID**     | ID unik untuk setiap produk.                                                 |
| **Product_Name**   | Nama produk (Laptop, Smartphone, Tablet).                                    |
| **Category**       | Kategori produk (Electronics).                                               |
| **Demand**         | Jumlah permintaan produk per bulan.                                          |
| **Inventory**      | Jumlah stok yang tersedia saat ini.                                          |
| **Supplier_ID**    | ID pemasok.                                                                  |
| **Supplier_Name**  | Nama pemasok.                                                                |
| **Supplier_Cost**  | Biaya per unit dari pemasok.                                                 |
| **Lead_Time**      | Waktu pengiriman dari pemasok (dalam hari).                                  |
| **Holding_Cost**   | Biaya penyimpanan per unit per bulan.                                        |
| **Order_Cost**     | Biaya pemesanan per order (fixed).                                           |
| **Date**           | Tanggal pencatatan data.                                                     |

### Contoh Data
| Product_ID | Product_Name | Category   | Demand | Inventory | Supplier_ID | Supplier_Name           | Supplier_Cost | Lead_Time | Holding_Cost | Order_Cost | Date       |
|------------|--------------|------------|--------|-----------|-------------|-------------------------|---------------|-----------|--------------|------------|------------|
| P123       | Laptop       | Electronics| 200    | 50        | S001        | GlobalTech Supplies     | 500           | 7         | 10           | 100        | 2023-03-15 |
| P456       | Smartphone   | Electronics| 150    | 30        | S002        | ElectroWorld Distributors| 300          | 5         | 8            | 100        | 2023-05-20 |
| P789       | Tablet       | Electronics| 100    | 20        | S003        | GadgetHub Inc.          | 200           | 10        | 5            | 100        | 2023-07-10 |

## Pertanyaan Analisis (Analytics Questions)
1. Berapa **jumlah pesanan optimal (EOQ)** untuk setiap produk?
2. Berapa **total biaya** yang harus dikeluarkan untuk setiap produk?
3. Bagaimana **lead time** memengaruhi tingkat inventaris?
4. Apakah ada pola **permintaan musiman** yang dapat diidentifikasi?
5. Bagaimana cara mengoptimalkan **tingkat inventaris** untuk menghindari stockout dan kelebihan stok?

## Metrik Kinerja (Key Performance Indicators - KPIs)
1. **Economic Order Quantity (EOQ):**  
   Jumlah pesanan optimal untuk setiap produk.

2. **Total Biaya:**  
   Biaya pemesanan + biaya penyimpanan.

3. **Service Level:**  
   Persentase permintaan pelanggan yang dapat dipenuhi tanpa stockout.

4. **Inventory Turnover Ratio:**  
   Seberapa cepat inventaris terjual dan diganti.

5. **Lead Time Variability:**  
   Variasi waktu pengiriman dari pemasok.

## Cara Menggunakan Dataset
1. **Hitung EOQ (Economic Order Quantity):**  
   Gunakan kolom `Demand`, `Holding_Cost`, dan `Order_Cost` untuk menghitung EOQ.

2. **Hitung Total Biaya:**  
   Gunakan kolom `Demand`, `EOQ`, `Holding_Cost`, dan `Order_Cost` untuk menghitung total biaya.

3. **Analisis Lead Time:**  
   Gunakan kolom `Lead_Time` untuk memastikan tidak ada stockout.

4. **Visualisasi Data:**  
   Gunakan library seperti `matplotlib` atau `seaborn` untuk memvisualisasikan hubungan antara fitur-fitur.