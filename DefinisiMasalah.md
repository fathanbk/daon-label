Nama Kelompok :
1. Aldy Syachranie (1313621012)
2. Danan Danurwenda Adi Kusuma (1313621017)
3. Fathan Bainal Kaffi (1313621037)
4. Muhammad Alfin Khaerudin (1313621003)

Kode yang kami buat merupakan upaya untuk mengklasifikasikan daun ke dalam spesies berdasarkan panjang, lebar, dan area daun, sesuai dengan dataset yang telah diberikan. Masalah utamanya ialah mengklasifikasikan daun ke dalam spesies berdasarkan panjang, lebar, dan area daun. Data masukan atau data set yang diberikan adalah data daun yang memiliki kolom 'leaf width' (lebar daun), 'leaf length' (panjang daun), 'species' (spesies daun). Disini kami melakukan pembacaan data awal yang terletak di 'dataset/data.csv'. Selanjutnya kami melakukan pemrosesan data untuk mengubah tipe data kolom-kolom yang sesuai dengan studi kasus yang diberikan. Kami juga menyimpan beberapa studi kasus dalam file csv yang isinya berbeda-beda sesuai dengan studi kasus yang diberikan. Karena ada beberapa studi kasus yang perlu dipecahkan, disini kami memberikan beberapa opsi menu untuk analisis yang berbeda, diantaranya:
1. Menambahkan data baru ke data awal dengan kolom yang sama.
2. Menebak spesies dari data baru dengan menghilangkan salah satu kolom.
3. Menebak spesies dari data baru dengan menambah satu kolom baru untuk semua data.
4. Menebak spesies dari data baru dengan spesies baru yang juga ditambahkan.

Untuk lebih lanjut disini kami membagi beberapa file secara terpisah dengan pendefinisian file-filenya sebagai berikut.

1. File leaf.py:
- File ini berisi definisi kelas Daon, yang digunakan untuk mewakili objek daun dengan berbagai atribut seperti lebar, panjang, spesies, dan tambahan (menyesuaikan dari suatu studi kasus). 
- Kelas Daon memiliki metode define_species yang berusaha untuk mengidentifikasi spesies daun berdasarkan lebar dan panjangnya. Metode ini mencoba mencocokkan ukuran daun dengan kisaran yang telah ditentukan untuk setiap spesies. 
Definisi masalah: Menentukan spesies daun berdasarkan ukuran (lebar dan panjang) dan atribut lainnya, seperti bentuk tambahan, jika ada penyesuaian dari sebuah studi kasus.

2. File species.py:
File ini berisi definisi kelas Species, yang digunakan untuk membuat objek yang mewakili spesies daun. Setiap objek Species memiliki atribut yang menyatakan batasan panjang dan lebar yang sesuai dengan spesies tersebut.
Definisi masalah: Mendefinisikan spesies daun dengan batasan panjang dan lebar yang dapat digunakan untuk mengklasifikasikan daun berdasarkan ukuran mereka.

3. File math2.py:
File ini berisi fungsi make_range, yang mencoba mengelompokkan angka-angka ke dalam kategori berdasarkan rentang yang diberikan. Fungsi ini dapat digunakan untuk mengelompokkan data lebar dan panjang daun ke dalam kategori tertentu.
Definisi masalah: Mengelompokkan angka-angka (seperti lebar dan panjang daun) ke dalam kategori berdasarkan rentang yang telah ditentukan.

4. File init.py:
File ini adalah file utama yang menghubungkan komponen-komponen di atas dan berisi logika untuk menyelesaikan beberapa definisi masalah yang mungkin terkait dengan analisis spesies daun. Pada file ini akan menghubungkan dan mengkoordinasikan berbagai komponen dalam proyek analisis spesies daun. File ini memulai dengan mengimpor modul dan kelas yang akan digunakan dalam proyek ini, termasuk Daon dari leaf.py, Species dari species.py, dan fungsi make_range dari math2.py. Ini adalah langkah awal yang diperlukan untuk mengakses fungsionalitas dari modul-modul tersebut. Selanjutnya pada file ini terdapat fungsi labelling yang dimana fungsi ini akan menerima data dalam bentuk daftar (list) dan mengonversinya menjadi objek Daon dengan berbagai atribut, seperti lebar, panjang, spesies, dan tambahan (jika ada). Artinya definisi masalah dari fungsi labelling ialah dapat mengonversi data mentah menjadi objek Daon yang dapat digunakan untuk analisis lebih lanjut. Selanjutnya kami membuat fungsi process_data. Fungsi ini menerima data dalam bentuk dataframe (seperti yang diambil dari pandas) dan mengubah tipe data kolom-kolom tertentu ke tipe data yang sesuai (misalnya, float untuk lebar dan panjang daun, dan string untuk spesies) dengan pendefinisian masalah dapat memastikan bahwa data yang digunakan untuk analisis memiliki tipe data yang benar. Selanjutnya kami membuat fungsi menu yang dimana fungsi ini digunakan untuk menampilkan menu pilihan kepada pengguna. Pengguna dapat memilih salah satu opsi yang sesuai dengan masalah yang ingin diatasi. Artinya definisi masalanya memungkinkan pengguna untuk memilih jenis analisis yang ingin dilakukan. Dan yang terakhir ada fungsi main. Fungsi ini adalah inti dari program dan mengatasi berbagai masalah analisis spesies daun sesuai dengan pilihan menu yang diberikan oleh pengguna. Fungsi ini mencakup pemrosesan data, pengolahan spesies, perhitungan kisaran lebar dan panjang daun, dan pemilihan spesies untuk data baru.
Definisi masalah yang diatasi dalam file ini termasuk:
- Menentukan spesies daun berdasarkan data baru dengan kolom yang ada.
- Menebak spesies daun untuk data baru ketika salah satu kolom dihilangkan.
- Menebak spesies daun untuk data baru ketika satu kolom tambahan ditambahkan untuk semua data yang ada.
- Menebak spesies daun untuk data baru ketika ada golongan spesies baru.
Dimana nanti setiap studi kasus yang diperlukan itu dibentuk secara pilihan yang nantinya akan dieksekusi jika kita memilih kasusnya.