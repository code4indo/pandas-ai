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

### Visualisasi Data

Pandas secara native memiliki kemampuan untuk melakukan visualisasi data sederhana, namun untuk visualisasi yang lebih kompleks biasanya digabungkan dengan library seperti Matplotlib atau Seaborn. Berikut ini beberapa fungsi yang paling umum digunakan dalam visualisasi data:

| Fungsi  | Deskripsi | Prompt/Instruksi |
| ------------- | ------------- | ------------- |
| `df['column'].plot(kind='type')` | Membuat plot dasar dari kolom tertentu. | "Buat plot jenis 'type' dari kolom ini." |
| `df['column'].hist(bins=n)` | Membuat histogram dari kolom tertentu. | "Buat histogram dari kolom ini dengan n bins." |
| `df.boxplot(column='column')` | Membuat boxplot dari kolom tertentu. | "Buat boxplot dari kolom ini." |
| `df.plot.scatter(x='column1', y='column2')` | Membuat scatter plot dari dua kolom. | "Buat scatter plot dengan kolom ini sebagai sumbu x dan kolom itu sebagai sumbu y." |
| `df['column'].value_counts().plot.bar()` | Membuat bar plot dari frekuensi nilai dalam kolom. | "Buat bar plot dari frekuensi nilai dalam kolom ini." |
| `sns.countplot(x='column', data=df)` | Membuat countplot (sejenis bar plot) dengan Seaborn. | "Buat countplot dari kolom ini menggunakan Seaborn." |
| `sns.heatmap(df.corr(), annot=True)` | Membuat heatmap dari korelasi antar kolom dalam DataFrame. | "Buat heatmap dari korelasi antar kolom dalam DataFrame ini." |
| `sns.pairplot(df)` | Membuat pairplot dari semua kolom dalam DataFrame. | "Buat pairplot dari semua kolom dalam DataFrame ini." |
| `plt.hist(df['column'], bins=n)` | Membuat histogram dengan Matplotlib. | "Buat histogram dari kolom ini dengan n bins menggunakan Matplotlib." |
| `sns.boxplot(x='column1', y='column2', data=df)` | Membuat boxplot dengan Seaborn. | "Buat boxplot dengan kolom ini sebagai sumbu x dan kolom itu sebagai sumbu y menggunakan Seaborn." |

Perlu dicatat bahwa fungsi-fungsi ini hanya sebagian kecil dari yang tersedia dalam library Python untuk visualisasi data. Selalu ingat untuk memahami data Anda dan memilih jenis visualisasi yang paling tepat.

### Jenis Plot Library Matplotlib

Matplotlib adalah library visualisasi di Python yang sangat serbaguna dan dapat digunakan untuk membuat berbagai jenis plot atau grafik. Berikut adalah beberapa jenis plot yang umum digunakan, beserta fungsinya:

| Jenis Plot | Fungsi |
|------------|--------|
| Line Plot | Biasa digunakan untuk menampilkan tren data sepanjang waktu. Setiap titik data dihubungkan oleh garis lurus.|
| Bar Plot/Bar Chart | Digunakan untuk membandingkan kuantitas variabel kategorikal. Dalam beberapa kasus, dapat juga digunakan untuk menampilkan perubahan variabel sepanjang waktu.|
| Histogram | Digunakan untuk memvisualisasikan distribusi data. Ini adalah cara yang baik untuk memahami distribusi dan frekuensi data numerik.|
| Scatter Plot | Digunakan untuk memvisualisasikan hubungan antara dua variabel numerik. Setiap titik pada plot mewakili satu observasi dalam dataset.|
| Pie Chart | Digunakan untuk memvisualisasikan proporsi kategori dalam keseluruhan. Setiap irisan pie mewakili satu kategori.|
| Box Plot | Digunakan untuk menampilkan statistik ringkasan seperti kuartil dan outlier. Box plot adalah cara yang baik untuk menggambarkan variabilitas data.|
| Area Plot | Digunakan untuk memvisualisasikan distribusi data sepanjang waktu atau variabel lain. Merupakan variasi dari line plot, di mana area di bawah garis diisi.|
| Heatmap | Digunakan untuk memvisualisasikan matriks korelasi atau tabel frekuensi silang. Warna berbeda merepresentasikan level intensitas data.|
| Contour Plot | Digunakan untuk memvisualisasikan tiga variabel numerik dalam dua dimensi. Satu variabel diplot pada sumbu x dan y, dan variabel ketiga diwakili oleh kontur.|

Perlu dicatat bahwa jenis plot yang tepat akan bergantung pada jenis data dan pertanyaan penelitian atau analisis yang ingin dijawab.

### Jenis Plot Library Seaborn
Seaborn adalah library visualisasi data di Python yang dibangun di atas Matplotlib. Seaborn memperluas fungsi Matplotlib dan memudahkan pembuatan plot yang lebih kompleks dan informatif. Berikut beberapa jenis plot yang dapat dibuat dengan Seaborn dan fungsinya:

| Jenis Plot | Fungsi |
|------------|--------|
| Distplot | Memvisualisasikan distribusi univariat (satu variabel) dalam bentuk histogram dan KDE (Kernel Density Estimation).|
| Jointplot | Memvisualisasikan hubungan antara dua variabel dan distribusi masing-masing variabel. Dapat digunakan untuk membuat scatterplot, hexbin plot, dan banyak jenis plot lainnya.|
| Pairplot | Membuat matriks plot untuk memvisualisasikan hubungan bivariat antara setiap pasangan variabel dalam dataset. |
| Boxplot | Sama seperti di Matplotlib, Boxplot di Seaborn digunakan untuk menampilkan statistik ringkasan seperti kuartil dan outlier.|
| Violinplot | Mirip dengan boxplot, tetapi juga mencakup kernel density estimation (KDE) untuk menunjukkan distribusi data.|
| Heatmap | Digunakan untuk memvisualisasikan data matriks. Warna berbeda merepresentasikan level intensitas data.|
| Barplot | Membandingkan kuantitas variabel kategorikal. Dalam beberapa kasus, dapat juga digunakan untuk menampilkan perubahan variabel sepanjang waktu.|
| Countplot | Spesifik untuk Seaborn, plot ini digunakan untuk menunjukkan jumlah pengamatan dalam setiap bin kategorikal. |
| FacetGrid | Digunakan untuk memvisualisasikan distribusi variabel dan hubungan antar variabel dalam dataset, menggunakan subplot yang dipetakan ke kolom dan baris kategori.|
| lmplot | Plot ini digunakan untuk menampilkan model regresi linier antara dua variabel dengan scatterplot dan garis regresi.|

Meski banyak plot di Seaborn yang mirip dengan Matplotlib, Seaborn memiliki fitur lebih untuk mempermudah analisis statistik dan pengeksplorasi data.




