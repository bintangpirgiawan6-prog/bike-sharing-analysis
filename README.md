# BikeScope - Bike Sharing Analysis

## Deskripsi

BikeScope merupakan dashboard analisis data yang dibuat untuk memahami pola penggunaan layanan bike sharing berdasarkan waktu, status hari kerja, dan kondisi cuaca.

Analisis ini menggunakan Bike Sharing Dataset yang terdiri dari data penyewaan sepeda secara harian dan per jam.

## Pertanyaan Bisnis

1. Bagaimana pola jumlah penyewaan sepeda berdasarkan jam dan status hari kerja selama periode Januari 2011 hingga Desember 2012?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca selama periode Januari 2011 hingga Desember 2012?

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
- Insight hasil analisis.

## Struktur Folder

```text
submission/
├── dashboard/
│   └── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── Proyek_Analisis_Data.ipynb
├── README.md
├── requirements.txt
└── url.txt