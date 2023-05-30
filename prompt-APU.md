### Jenis: Structuring

| Tujuan | Prompt |
| --- | --- |
| Identifikasi Transaksi | "Berikan daftar transaksi yang dilakukan dalam jumlah relatif kecil namun dengan frekuensi yang tinggi. Simpan hasilnya dalam format CSV dengan nama 'Transaksi_Frekuensi_Tinggi.csv'." |
| Analisis Transaksi | "Analisis transaksi yang dilakukan dalam jumlah relatif kecil namun dengan frekuensi yang tinggi. Identifikasi pola dan tren yang mungkin menunjukkan aktivitas structuring. Simpan hasil analisis dalam format CSV dengan nama 'Analisis_Transaksi_Frekuensi_Tinggi.csv'." |
| Deteksi Structuring | "Gunakan algoritma deteksi anomali untuk mengidentifikasi transaksi yang mungkin merupakan structuring. Transaksi ini biasanya dilakukan dalam jumlah relatif kecil namun dengan frekuensi yang tinggi. Simpan hasil deteksi dalam format CSV dengan nama 'Deteksi_Structuring.csv'." |
| Laporan Transaksi Mencurigakan | "Buat laporan dari transaksi yang dicurigai sebagai structuring. Laporan ini harus mencakup detail transaksi dan alasan mengapa transaksi tersebut dicurigai sebagai structuring. Simpan laporan dalam format CSV dengan nama 'Laporan_Transaksi_Mencurigakan.csv'." |

### Jenis Deteksi: Smurfing 


| Tujuan | Prompt | Jenis Visualisasi |
| --- | --- | --- |
| Identifikasi Transaksi | "Berikan daftar transaksi yang dilakukan menggunakan beberapa rekening atas nama individu yang berbeda-beda untuk kepentingan satu orang tertentu. Simpan hasilnya dalam format CSV dengan nama 'Transaksi_Smurfing.csv'." | Diagram batang atau pie untuk menunjukkan jumlah transaksi per rekening. |
| Analisis Transaksi | "Analisis transaksi yang dilakukan menggunakan beberapa rekening atas nama individu yang berbeda-beda untuk kepentingan satu orang tertentu. Identifikasi pola dan tren yang mungkin menunjukkan aktivitas smurfing. Simpan hasil analisis dalam format CSV dengan nama 'Analisis_Transaksi_Smurfing.csv'." | Heatmap atau diagram sebar untuk menunjukkan pola transaksi antara berbagai rekening. |
| Deteksi Smurfing | "Gunakan algoritma deteksi anomali untuk mengidentifikasi transaksi yang mungkin merupakan smurfing. Transaksi ini biasanya dilakukan menggunakan beberapa rekening atas nama individu yang berbeda-beda untuk kepentingan satu orang tertentu. Simpan hasil deteksi dalam format CSV dengan nama 'Deteksi_Smurfing.csv'." | Diagram batang atau pie untuk menunjukkan jumlah transaksi yang dicurigai sebagai smurfing per rekening. |
| Laporan Transaksi Mencurigakan | "Buat laporan dari transaksi yang dicurigai sebagai smurfing. Laporan ini harus mencakup detail transaksi dan alasan mengapa transaksi tersebut dicurigai sebagai smurfing. Simpan laporan dalam format CSV dengan nama 'Laporan_Transaksi_Mencurigakan_Smurfing.csv'." | Diagram batang atau pie untuk menunjukkan jumlah transaksi yang dicurigai sebagai smurfing per rekening. |

### Jenis: Transaksi yang dilakukan secara tunai dalam jumlah di luar kebiasaan

| Tujuan | Prompt | Jenis Visualisasi |
| --- | --- | --- |
| Identifikasi Transaksi | "Berikan daftar transaksi yang dilakukan secara tunai dalam jumlah di luar kebiasaan yang dilakukan nasabah. Simpan hasilnya dalam format CSV dengan nama 'Transaksi_Tunai_Di_Luar_Kebiasaan.csv'." | Diagram batang atau pie untuk menunjukkan jumlah transaksi tunai per nasabah. |
| Analisis Transaksi | "Analisis transaksi yang dilakukan secara tunai dalam jumlah di luar kebiasaan yang dilakukan nasabah. Identifikasi pola dan tren yang mungkin menunjukkan aktivitas mencurigakan. Simpan hasil analisis dalam format CSV dengan nama 'Analisis_Transaksi_Tunai_Di_Luar_Kebiasaan.csv'." | Heatmap atau diagram sebar untuk menunjukkan pola transaksi tunai antara berbagai nasabah. |
| Deteksi Transaksi Mencurigakan | "Gunakan algoritma deteksi anomali untuk mengidentifikasi transaksi tunai yang mungkin mencurigakan. Transaksi ini biasanya dilakukan dalam jumlah di luar kebiasaan yang dilakukan nasabah. Simpan hasil deteksi dalam format CSV dengan nama 'Deteksi_Transaksi_Tunai_Mencurigakan.csv'." | Diagram batang atau pie untuk menunjukkan jumlah transaksi tunai yang dicurigai sebagai mencurigakan per nasabah. |
| Laporan Transaksi Mencurigakan | "Buat laporan dari transaksi tunai yang dicurigai sebagai mencurigakan. Laporan ini harus mencakup detail transaksi dan alasan mengapa transaksi tersebut dicurigai sebagai mencurigakan. Simpan laporan dalam format CSV dengan nama 'Laporan_Transaksi_Tunai_Mencurigakan.csv'." | Diagram batang atau pie untuk menunjukkan jumlah transaksi tunai yang dicurigai sebagai mencurigakan per nasabah. |

### Hasil Anlisis Kolom pada data Dummy Hackathon

Menganalisis transaksi mencurigakan dan pencucian uang melibatkan pembelajaran mendalam tentang pola-pola tertentu dalam data. Kolom-kolom yang diberikan memiliki informasi yang berpotensi bisa digunakan untuk mendeteksi kegiatan mencurigakan. 

Berikut adalah beberapa ide untuk memanfaatkan kolom-kolom yang tersedia:

1. **Analisis Statistik Deskriptif**: Lakukan analisis statistik deskriptif pada kolom 'nilaitransaksi'. Dapatkan nilai rata-rata, median, modus, dan rentang transaksi. Transaksi dengan nilai yang sangat tinggi atau rendah bisa menjadi indikator aktivitas mencurigakan.

2. **Analisis Frekuensi Transaksi**: Periksa frekuensi transaksi berdasarkan 'NamaPEASource' dan 'NamaPEADestination'. Pelaku pencucian uang mungkin akan melakukan banyak transaksi dalam waktu yang relatif singkat.

3. **Analisis Jenis Transaksi**: Analisis frekuensi jenis transaksi ('jenis_transaksi') dapat menunjukkan apakah ada pola tertentu yang diikuti oleh pelaku pencucian uang.

4. **Analisis Geografis**: Pelaku pencucian uang sering menggunakan transaksi lintas negara untuk menyembunyikan asal usul dana mereka. Analisis frekuensi transaksi berdasarkan 'negaraSource' dan 'NegaraDest' bisa mengungkapkan pola ini.

5. **Analisis Waktu Transaksi**: Analisis pola waktu transaksi ('tgl_transaksi') mungkin bisa membantu mendeteksi aktivitas mencurigakan. Misalnya, transaksi yang terjadi di luar jam kerja atau pada saat-saat tertentu dapat menjadi tanda peringatan.

6. **Analisis Tindakan dan Alasan Pelaporan**: Kolom 'tindakan_PP' dan 'alasan_pelaporan' dapat memberikan wawasan tentang apa yang telah dilakukan PP sebelumnya dan mengapa mereka melaporkannya. Data ini bisa membantu dalam membuat model prediktif untuk deteksi pencucian uang.

7. **Analisis Indikator Pelaporan**: Kolom 'indikator_pelaporan' mungkin memiliki indikator spesifik yang dapat dipantau untuk deteksi dini aktivitas mencurigakan.

8. **Analisis Hubungan Source dan Destination**: Dengan melihat hubungan antara 'tipe_source' dan 'tipe_dest', kita dapat menemukan pola atau anomali dalam aliran uang.

9. **Analisis Tekstual**: Kolom seperti 'ttr_description' dan 'ttr_comments' dapat dianalisis menggunakan teknik NLP (Natural Language Processing) untuk mengidentifikasi kata kunci atau frase yang mencurigakan.

10. **Analisis Pekerjaan**: Pekerjaan ('pekerjaanSource' dan 'pekerjaanDest') mungkin dapat digunakan untuk mengidentifikasi profesi atau industri yang lebih mungkin terlibat dalam pencucian uang.

Setelah menemukan pola atau indikator potensial pencucian uang, Anda dapat menggunakan teknik machine learning untuk membuat model prediktif. Misalnya, Anda bisa menggunakan algoritma klasifikasi untuk memprediksi apakah transaksi tertentu mencurigakan atau tidak berdasarkan fitur yang telah Anda identifikasi.



**prompt untuk dicoba**
1.	Analisis Statistik Deskriptif
Lakukan perhitungan statistik deskriptif dengan menghitung nilai rata-rata, nilai median, nilai modus, dan rentang transaksi berdasarkan nilai transaksi antara PEASource dan PEADestination yang menghasilkan rentang sangat tinggi atau sangat rendah, lalu buat dalam daftar Kemudian buat grafiknya.

2.	Analisis Frekuensi Transaksi 
Tampilkan transaksi yang banyak dilakukan dalam waktu yang relatif singkat berdasarkan NamaPEASource dan NamaPEADestination yang beresiko tinggi sebagai pencucian uang

3.	Analisis Jenis Transaksi
Temukan pola-pola tertentu yang menunjukkan modus dari pencucian uang berdasarkan jenis laporan gambarkan dalam sebuah mindmap
Temukan pola-pola tertentu yang menunjukkan modus dari pendanaan teroris gambarkan dalam sebuah mindmap
Temukan pola-pola tertentu yang menunjukkan modus dari pencucian uang yang dilakukan antar lembaga selain lembaga keuangan dan gambarkan dalam sebuah mindmap

4.	Analisis Geografis
Temukan pola-pola tertentu yang menunjukkan modus dari pencucian uang lintas negara antara negaraSource dan NegaraDest dengan nilai transaksi di atas 3 milyar dalam waktu yang sangat dekat
