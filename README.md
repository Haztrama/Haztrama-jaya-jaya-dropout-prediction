# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

**Nama:** Hafiz Putra Mahesta  
**Email:** phafiz726@gmail.com  
**ID Dicoding:** Hafiz Putra Mahesta  

## Business Understanding

**Konteks Masalah:** Jaya Jaya Institut adalah institusi pendidikan yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik. Namun, institusi ini menghadapi masalah serius terkait tingginya angka mahasiswa yang tidak menyelesaikan pendidikan alias putus kuliah (*dropout*). Tingginya angka *dropout* ini berdampak negatif pada performa dan reputasi institusi.

**Tujuan Proyek:** 1. Mengidentifikasi faktor-faktor utama yang memengaruhi keputusan mahasiswa untuk *dropout*.
2. Membangun model *Machine Learning* untuk mendeteksi sedini mungkin mahasiswa yang berisiko *dropout*.
3. Membuat *dashboard* interaktif untuk memonitor performa mahasiswa secara keseluruhan.

## Conclusion

Berdasarkan hasil *Exploratory Data Analysis* (EDA) dan pemodelan *Machine Learning* (menggunakan algoritma *Random Forest*), dapat ditarik beberapa kesimpulan utama:
1. **Faktor Finansial Sangat Krusial:** Mahasiswa yang menunggak biaya kuliah (UKT tidak *up-to-date*) memiliki tingkat *dropout* yang sangat ekstrem dibandingkan mahasiswa yang melunasi biaya kuliah. 
2. **Performa Akademik Awal Menentukan:** Mahasiswa yang berakhir *dropout* rata-rata memiliki nilai yang jauh lebih rendah (atau bahkan 0) pada evaluasi Semester 1, mengindikasikan bahwa mereka sudah pasif atau kesulitan beradaptasi sejak awal perkuliahan.
3. **Model Prediksi Berhasil Dibangun:** Model *Random Forest Classifier* telah berhasil dilatih dan mampu mengklasifikasikan mahasiswa berisiko *dropout* dengan tingkat *Recall* yang sangat baik, sehingga sangat cocok digunakan sebagai sistem deteksi dini.

## Recomendation Action Items

Untuk menekan angka *dropout*, berikut adalah rekomendasi tindakan (*Action Items*) bagi manajemen Jaya Jaya Institut:
1. **Intervensi Finansial Dini:** Memberikan peringatan dini dan menawarkan opsi keringanan pembayaran (cicilan) atau program beasiswa khusus bagi mahasiswa yang mulai terdeteksi menunggak biaya kuliah di semester pertama.
2. **Program Bimbingan Akademik Wajib:** Mewajibkan sesi bimbingan konseling akademik bagi mahasiswa yang memiliki nilai di bawah standar pada ujian pertengahan Semester 1.
3. **Pemanfaatan Sistem Prediksi:** Mengintegrasikan *prototype Machine Learning* ini ke dalam sistem informasi akademik kampus agar staf akademik mendapatkan notifikasi otomatis ("Merah/Berisiko Dropout") saat profil mahasiswa baru memenuhi kriteria risiko tinggi.

## Tautan Proyek

- **Streamlit Prototype (Live):** [https://jayajaya-student-monitoring.streamlit.app/](https://jayajaya-student-monitoring.streamlit.app/)
- **Metabase Dashboard:** File `metabase.db.mv.db` telah disertakan dalam submission ini.
  - *Email Login:* `root@mail.com`
  - *Password Login:* `root123`

## Cara Menjalankan Prototype Machine Learning Secara Lokal

Jika ingin menjalankan aplikasi Streamlit ini di komputer lokal, ikuti langkah-langkah berikut:

1. Pastikan Anda telah menginstal Python di komputer.
2. *Clone* atau ekstrak *repository* / folder proyek ini.
3. Buka *Command Prompt* atau Terminal, lalu navigasikan ke folder proyek.
4. Instal semua *library* pendukung dengan menjalankan perintah:
   ```bash
   pip install -r requirements.txt
   ```
5. Jalankan aplikasi Streamlit dengan perintah:
   ```bash
   streamlit run app.py
   ```
6. Aplikasi akan terbuka secara otomatis di browser pada alamat http://localhost:8501
