Prompt Dasar pada Pandas 
Berikut tabel yang telah ditambahkan kolom berisi instruksi atau prompt dari setiap fungsi:

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
