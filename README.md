# Bike Sharing Dashboard 🚲

Dashboard interaktif untuk menganalisis pola penyewaan sepeda berdasarkan jam, status hari kerja, dan kondisi cuaca selama periode Januari 2011 hingga Desember 2012.


## 🔗 Dashboard Online

Dashboard interaktif dapat diakses melalui tautan berikut:
[**Bike Sharing Dashboard**](https://bike-sharing-analysis-bintangpirgiawan.streamlit.app/)


## Pertanyaan Bisnis

1. Bagaimana pola jumlah penyewaan sepeda berdasarkan jam dan status hari kerja?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca?

## Setup Environment - Anaconda

Buat environment Python dan aktifkan environment tersebut.

```bash
conda create --name bike-sharing python=3.11
conda activate bike-sharing
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

Buka terminal pada folder utama proyek, kemudian jalankan perintah berikut.

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Instal seluruh library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

## Run Streamlit App

Pastikan terminal berada di folder utama proyek dan environment sudah aktif. Jalankan dashboard menggunakan perintah:

```bash
streamlit run dashboard.py
```

Setelah aplikasi berjalan, buka alamat lokal yang muncul di terminal, biasanya `http://localhost:8501`.

## Fitur Dashboard

- Visualisasi pola penyewaan sepeda berdasarkan jam dan status hari kerja.
- Visualisasi rata-rata penyewaan sepeda berdasarkan kondisi cuaca.
- Filter interaktif untuk membantu pengguna mengeksplorasi data penyewaan sepeda.

## Struktur Folder

```text
bike-sharing-analysis/
├── dashboard.py
├── day.csv
├── hour.csv
├── main_data.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook


## Project Files

- `dashboard.py` — Kode aplikasi dashboard Streamlit.
- `main_data.csv` — Dataset gabungan yang digunakan dashboard.
- `day.csv` — Dataset penyewaan sepeda harian.
- `hour.csv` — Dataset penyewaan sepeda per jam.
- `notebook.ipynb` — Notebook proses analisis data.
- `requirements.txt` — Daftar library Python yang diperlukan.
- `url.txt` — File informasi tautan proyek.
