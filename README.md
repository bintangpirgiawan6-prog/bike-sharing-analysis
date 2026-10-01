# BikeScope - Bike Sharing Analysis

## Deskripsi

BikeScope merupakan dashboard analisis data yang dibuat untuk memahami pola penggunaan layanan bike sharing berdasarkan waktu, status hari kerja, dan kondisi cuaca.

Analisis ini menggunakan Bike Sharing Dataset yang terdiri dari data penyewaan sepeda berdasarkan harian dan per jam.

## Pertanyaan Bisnis

1. Pada jam berapa rata-rata jumlah penyewaan sepeda paling tinggi dan paling rendah?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca?

## Dataset

Dataset yang digunakan adalah Bike Sharing Dataset yang terdiri dari:

- `day.csv` — data penyewaan sepeda secara harian.
- `hour.csv` — data penyewaan sepeda berdasarkan jam.

## Fitur Dashboard

Dashboard menyediakan beberapa fitur:

- Filter berdasarkan tahun.
- Filter berdasarkan status hari kerja.
- Total jumlah penyewaan.
- Rata-rata jumlah penyewaan harian.
- Informasi jam dengan rata-rata penyewaan tertinggi.
- Informasi kondisi cuaca dengan rata-rata penyewaan tertinggi.
- Visualisasi pola penyewaan berdasarkan jam.
- Visualisasi rata-rata penyewaan berdasarkan kondisi cuaca.

## Cara Menjalankan Dashboard

### 1. Clone atau download repository

Pastikan seluruh file project berada dalam satu folder.

### 2. Install library

Buka terminal pada folder project kemudian jalankan:

```bash
pip install -r requirements.txt