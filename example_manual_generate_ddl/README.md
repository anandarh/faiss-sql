# Aplikasi Pencarian dan Validasi Query SQL dengan FAISS dan LangChain

Aplikasi ini menggunakan FAISS (Facebook AI Similarity Search) dan LangChain dengan Google Generative AI untuk mencari dan memvalidasi query SQL berdasarkan pertanyaan pengguna.

## Persyaratan Sistem

- Python 3.11 atau lebih baru
- Pip (pengelola paket Python)
- Akses ke Google Generative AI API

## Instalasi

1. Clone repositori ini ke komputer lokal Anda
2. Buat virtual environment Python:
   ```
   python -m venv myenv
   ```
3. Aktifkan virtual environment:
   - Windows: `myenv\Scripts\activate`
   - macOS/Linux: `source myenv/bin/activate`
4. Instal dependensi yang diperlukan:
   ```
   pip install -r requirements.txt
   ```
5. Siapkan API key Google Generative AI Anda di file `.env` atau langsung di `main.py`

## Penggunaan

Jalankan aplikasi dengan perintah:
```
python main.py
```

Setelah aplikasi berjalan, Anda dapat memasukkan pertanyaan dalam bahasa alami tentang data stunting. Sistem akan:
1. Mencari query SQL yang paling relevan dengan pertanyaan Anda
2. Memvalidasi apakah query tersebut dapat menjawab pertanyaan Anda
3. Menjelaskan cara kerja query dan data yang akan dihasilkan

Ketik "exit" untuk keluar dari aplikasi.

## Struktur Proyek

- `main.py`: File utama yang menjalankan aplikasi
- `documents_sql.py`: Berisi kumpulan dokumen query SQL untuk berbagai pertanyaan terkait data stunting
- `documents_ddl.py`: Berisi definisi struktur database (DDL) yang digunakan dalam proyek
- `requirements.txt`: Daftar dependensi yang diperlukan

## Komponen Utama

### Vector Store dengan FAISS

Aplikasi ini menggunakan FAISS untuk menyimpan dan mencari embedding dari dokumen SQL. FAISS memungkinkan pencarian cepat berdasarkan kesamaan vektor, yang sangat berguna untuk menemukan query SQL yang paling relevan dengan pertanyaan pengguna.

### LangChain dan Google Generative AI

Aplikasi menggunakan LangChain dengan model Google Generative AI untuk:
1. Menghasilkan embedding dari pertanyaan pengguna dan dokumen SQL
2. Memvalidasi dan menjelaskan query SQL yang ditemukan

### Dokumen SQL dan DDL

Aplikasi ini berisi kumpulan dokumen SQL yang telah disiapkan untuk berbagai pertanyaan tentang data stunting di Indonesia, serta definisi struktur database yang digunakan.

## Catatan Tambahan

- Aplikasi ini dirancang khusus untuk data stunting di Indonesia
- Query SQL yang disediakan mencakup berbagai aspek data stunting, termasuk prevalensi stunting, jumlah balita stunting, anggaran penurunan stunting, dan banyak lagi
- Struktur database mencakup berbagai tabel terkait data stunting, kesehatan ibu dan anak, serta data pendukung lainnya
