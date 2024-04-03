### Fuzzy Logic Prediction System - Kemampuan Daya Lari 

Repositori ini berisi implementasi Python dari Sistem Prediksi Logika Fuzzy menggunakan library `scikit-fuzzy`. Sistem ini memprediksi kategori output berdasarkan tiga variabel input: jarak (`jarak`), waktu (`waktu`), dan detak jantung (`denyut`).

## Isi
1. [Pendahuluan](#pendahuluan)
2. [Ketergantungan](#ketergantungan)
3. [Penggunaan](#penggunaan)
4. [Penjelasan](#penjelasan)
5. [Referensi](#referensi)

## Pendahuluan
Logika fuzzy menyediakan cara untuk menangani informasi yang tidak pasti dan samar dalam proses pengambilan keputusan. Sistem ini menggunakan logika fuzzy untuk memprediksi kategori variabel output berdasarkan variabel input yang diberikan.

## Kebutuhan modul
modul berikut diperlukan untuk menjalankan kode:
- `numpy`
- `scikit-fuzzy`
- `pandas`

Anda dapat menginstalnya menggunakan pip:
`pip install numpy scikit-fuzzy pandas`

## Penggunaan
1. Klona repositori:
git clone https://github.com/yourusername/fuzzy-logic-prediction.git
2. Arahkan ke direktori repositori:
cd fuzzy-logic-prediction
3. Pastikan Anda memiliki file CSV bernama `data.csv` yang berisi data input.
4. Jalankan skrip Python:
python fuzzy_logic_prediction.py
5. Periksa file Excel yang dihasilkan bernama `hasil.xlsx` untuk melihat kategori yang diprediksi.

## Penjelasan
1. **Import Library**: Library yang diperlukan seperti `numpy`, `scikit-fuzzy`, dan `pandas` diimpor.

2. **Mendefinisikan Anteseden dan Konsekuen**: Anteseden (`jarak`, `waktu`, `denyut`) dan Konsekuen (`predikat`) didefinisikan bersama dengan fungsi keanggotaan mereka.

3. **Penentuan rules**: Seperangkat aturan fuzzy didefinisikan berdasarkan kebutuhan/fungsional.

4. **Membuat Sistem Kontrol**: Sistem kontrol dibuat menggunakan aturan yang telah didefinisikan.

5. **Membaca Data**: Data input dibaca dari file `data.csv`.

6. **Inferensi Fuzzy**: Untuk setiap titik data, inferensi fuzzy dilakukan untuk menentukan kategori yang diprediksi.

7. **Kategori Prediksi**: Nilai yang diprediksi dikategorikan menjadi 'rendah', 'sedang', atau 'tinggi' berdasarkan ambang batas yang telah ditentukan.

8. **Output**: Prediksi disimpan dalam DataFrame dan disimpan ke file Excel dengan nama `hasil.xlsx`.

## Referensi
- [Dokumentasi scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/)
- [Dokumentasi Pandas](https://pandas.pydata.org/docs/)
- [Dokumentasi NumPy](https://numpy.org/doc/)
