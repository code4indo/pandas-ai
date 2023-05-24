Prompt Dasar pada Pandas 

| Fungsi  | Deskripsi | Prompt/Instruksi |
| ------------- | ------------- | ------------- |
| `pd.read_csv('file.csv')` | Membaca file CSV dan mengubahnya menjadi DataFrame. | "Baca file CSV dan ubah menjadi DataFrame." |
| `pd.read_excel('file.xlsx')` | Membaca file Excel dan mengubahnya menjadi DataFrame. | "Baca file Excel dan ubah menjadi DataFrame." |
| `df.to_csv('file.csv')` | Menyimpan DataFrame ke file CSV. | "Simpan DataFrame ini ke file CSV." |
| `df.head(n)` | Menampilkan n baris pertama dari DataFrame. | "Tampilkan n baris pertama dari DataFrame ini." |
| `df.tail(n)` | Menampilkan n baris terakhir dari DataFrame. | "Tampilkan n baris terakhir dari DataFrame ini." |
| `df.shape` | Mengambil jumlah baris dan kolom dalam DataFrame. | "Berapa jumlah baris dan kolom dalam DataFrame ini?" |
| `df.info()` | Menampilkan informasi ringkas tentang DataFrame. | "Berikan informasi ringkas tentang DataFrame ini." |
| `df.describe()` | Menghasilkan statistik deskriptif dari DataFrame. | "Buat statistik deskriptif dari DataFrame ini." |
| `df.columns` | Mendapatkan nama kolom DataFrame. | "Apa saja nama kolom dalam DataFrame ini?" |
| `df.dtypes` | Mendapatkan tipe data untuk setiap kolom. | "Apa tipe data untuk setiap kolom dalam DataFrame ini?" |
| `df.isnull().sum()` | Menghitung jumlah nilai null dalam setiap kolom. | "Hitung jumlah nilai null dalam setiap kolom DataFrame ini." |
| `df['column'].value_counts()` | Menghitung frekuensi unik dari kolom tertentu. | "Hitung frekuensi unik dari kolom ini." |
| `df['column'].unique()` | Menampilkan nilai unik dalam kolom. | "Tampilkan nilai unik dalam kolom ini." |
| `df['column'].nunique()` | Menghitung jumlah nilai unik dalam kolom. | "Berapa banyak nilai unik dalam kolom ini?" |
| `df.sort_values('column')` | Mengurutkan DataFrame berdasarkan kolom tertentu. | "Urutkan DataFrame ini berdasarkan kolom ini." |
| `df.groupby('column').mean()` | Menghitung rata-rata berdasarkan grup dari kolom tertentu. | "Hitung rata-rata berdasarkan grup dari kolom ini." |
| `df.pivot_table(values='column1', index='column2')` | Membuat pivot table dari DataFrame. | "Buat pivot table dari DataFrame ini." |
| `df.drop('column', axis=1)` | Menghapus kolom tertentu dari DataFrame. | "Hapus kolom ini dari DataFrame." |
| `df['new_column'] = df['column1'] + df['column2']` | Membuat kolom baru dari operasi pada kolom lain. | "Buat kolom baru dengan menambahkan kolom ini dan kolom itu." |
| `df.rename(columns={'old_name': 'new_name'})` | Mengubah nama kolom dalam DataFrame. | "Ubah nama kolom ini menjadi nama baru." |

Dalam tugas prediksi data, library Pandas sering digunakan untuk mempersiapkan dan memproses data sebelum menggunakan algoritma Machine Learning. Berikut ini adalah beberapa fungsi yang paling umum digunakan dalam tugas prediksi data:

| Fungsi  | Deskripsi | Prompt/Instruksi |
| ------------- | ------------- | ------------- |
| `df['column'].astype('type')` | Mengubah tipe data dari kolom tertentu. | "Ubah tipe data dari kolom ini menjadi 'type'." |
| `df.dropna()` | Menghapus baris atau kolom dengan nilai null. | "Hapus baris atau kolom dengan nilai null dari DataFrame ini." |
| `df.fillna(value)` | Mengisi nilai null dengan nilai tertentu. | "Isi nilai null dalam DataFrame ini dengan 'value'." |
| `df['column'].replace('old_value', 'new_value')` | Mengganti nilai tertentu dalam kolom. | "Ganti 'old_value' dengan 'new_value' dalam kolom ini." |
| `df.apply(function)` | Menerapkan fungsi ke setiap elemen dalam DataFrame. | "Terapkan fungsi ini ke setiap elemen dalam DataFrame." |
| `df.merge(df2, on='column')` | Menggabungkan dua DataFrame berdasarkan kolom tertentu. | "Gabungkan DataFrame ini dengan df2 berdasarkan kolom ini." |
| `df['new_column'] = df['column1'].map(df2.set_index('column2')['column3'])` | Menggunakan peta untuk membuat kolom baru berdasarkan DataFrame lain. | "Buat kolom baru dengan memetakan kolom ini ke kolom dari df2." |
| `pd.get_dummies(df)` | Mengubah variabel kategori menjadi variabel dummy/indikator. | "Buat variabel dummy dari variabel kategori dalam DataFrame ini." |
| `df['column'].cut(bins, labels)` | Mengubah variabel kontinu menjadi variabel kategori. | "Ubah variabel kontinu ini menjadi variabel kategori dengan menggunakan bins dan labels ini." |
| `df.groupby('column').transform(function)` | Menerapkan fungsi ke setiap grup. | "Terapkan fungsi ini ke setiap grup berdasarkan kolom ini." |
| `df.set_index('column')` | Mengatur kolom tertentu sebagai indeks DataFrame. | "Atur kolom ini sebagai indeks DataFrame." |
| `df.reset_index()` | Mengatur indeks DataFrame ke indeks default. | "Atur indeks DataFrame ke indeks default." |
| `df['column'].rolling(window).mean()` | Menghitung rolling mean dari kolom tertentu. | "Hitung rolling mean dari kolom ini dengan menggunakan jendela waktu ini." |
| `df['column'].shift(periods)` | Menggeser nilai kolom ke depan atau ke belakang. | "Geser nilai dalam kolom ini sebanyak 'periods' posisi." |

Fungsi-fungsi di atas sangat umum digunakan dalam analisis dan prediksi data dengan Pandas. 
