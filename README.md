# Proyek Akhir Data Science: Menyelesaikan Permasalahan Institusi Pendidikan Jaya Jaya Institut

**Nama:** Hafiz Putra Mahesta  
**Email:** phafiz726@gmail.com  
**ID Dicoding:** Hafiz Putra Mahesta  

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan memiliki reputasi yang sangat baik. Namun, saat ini institusi sedang menghadapi tantangan internal berupa tingkat mahasiswa yang tidak menyelesaikan pendidikan alias putus kuliah (*dropout*) yang cukup tinggi. Tingginya angka ini berdampak negatif pada performa akademik, citra institusi, dan stabilitas finansial kampus.

Proyek ini bertujuan untuk menganalisis faktor-faktor penyebab tingginya angka *dropout* dan membangun model *machine learning* untuk memprediksi mahasiswa mana yang memiliki potensi tinggi untuk putus kuliah, sehingga staf akademik dapat melakukan langkah preventif sedini mungkin.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi masalah tingginya tingkat perputaran dan kegagalan studi mahasiswa (*dropout*). Tingginya angka putus kuliah ini sangat merugikan institusi karena menunjukkan adanya ketidakmaksimalan dalam sistem pendampingan mahasiswa. Oleh karena itu, institusi membutuhkan sebuah sistem yang dapat melakukan deteksi dini terhadap mahasiswa yang berisiko tinggi untuk *dropout*. Dengan adanya deteksi dini, pihak kampus (seperti dosen pembimbing akademik atau konselor) dapat mengambil tindakan pencegahan, bimbingan khusus, atau bantuan finansial yang lebih terarah sebelum mahasiswa tersebut benar-benar memutuskan untuk berhenti kuliah.

### Cakupan Proyek
- **Data Preparation:** Membersihkan data, menghapus status mahasiswa yang masih aktif (*Enrolled*) agar fokus pada klasifikasi biner, serta melakukan penyesuaian tipe data agar model *machine learning* menghasilkan prediksi yang akurat.
- **Exploratory Data Analysis (EDA):** Menganalisis pola data untuk menemukan akar masalah (seperti status pembayaran biaya kuliah dan nilai semester awal) agar manajemen kampus memahami alasan utama di balik tingginya angka *dropout*.
- **Pembuatan Dashboard:** Menyediakan alat pemantauan visual bagi manajemen kampus untuk memonitor metrik performa mahasiswa secara *real-time* tanpa perlu membaca data mentah.
- **Modeling & Deployment:** Menciptakan alat prediksi praktis berbasis *web* yang bisa digunakan oleh staf kampus sehari-hari untuk mendeteksi probabilitas *dropout* seorang mahasiswa baru.

### Sumber Data
Data yang digunakan dalam proyek ini merupakan dataset *students' performance* yang disediakan oleh Jaya Jaya Institut.
Tautan Dataset Asli: [Students' Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

### Setup Environment
Untuk menjalankan *notebook* dan aplikasi *machine learning* secara lokal, pastikan Anda telah menginstal semua *library* Python yang dibutuhkan. Anda bisa menginstalnya sekaligus dengan menjalankan perintah berikut di terminal:
```bash
pip install -r requirements.txt
```
## Business Dashboard
Dashboard bisnis telah dibuat menggunakan Metabase yang terhubung dengan database SQLite (jaya_jaya_institut.db). Dashboard ini memuat visualisasi kunci untuk membantu institusi mengidentifikasi pola dropout mahasiswa:
1. Persentase Status Mahasiswa (Pie Chart): Melihat proporsi status Graduate, Dropout, dan Enrolled.
2. Status vs Pembayaran UKT (Stacked Bar Chart): Analisis hubungan antara tunggakan biaya kuliah dengan probabilitas dropout.
3. Rata-rata Nilai Semester 1 (Bar Chart): Mengidentifikasi pengaruh performa akademik di awal perkuliahan terhadap keberhasilan studi.
4. Pengaruh Beasiswa terhadap Status (Stacked Bar Chart): Menganalisis bagaimana kepemilikan beasiswa berdampak pada tingkat retensi dan menekan probabilitas *dropout* mahasiswa.

Catatan untuk Reviewer: File metabase.db.mv.db telah dilampirkan dalam repositori/ZIP ini.
- Email Login: root@mail.com
- Password: root123

## Menjalankan Sistem Machine Learning
Model prediksi dikemas dalam bentuk prototipe web menggunakan antarmuka Streamlit.

Akses Langsung via Cloud:
Aplikasi telah di-deploy dan dapat diakses langsung melalui tautan berikut:
https://jayajaya-student-monitoring.streamlit.app/

Cara Menjalankan Secara Lokal:
1. Buka terminal/PowerShell dan arahkan ke direktori proyek.
2. Jalankan perintah berikut:
```bash
streamlit run app.py
```
3. Aplikasi akan terbuka secara otomatis di browser (biasanya di http://localhost:8501). Masukkan data parameter mahasiswa pada form yang tersedia untuk melihat prediksi apakah mahasiswa tersebut aman atau berisiko dropout.

## Conclusion
- Menjawab Permasalahan Bisnis: Sistem deteksi dini dropout mahasiswa telah berhasil dibangun. Pihak institusi kini memiliki alat prediksi (dashboard dan web app) yang dapat mengidentifikasi mahasiswa berisiko tinggi, sehingga intervensi berupa konseling atau bantuan finansial dapat diberikan lebih awal.
- Faktor Utama Dropout: Berdasarkan analisis EDA dan Feature Importance, mahasiswa yang menunggak biaya kuliah (Tuition fees up to date = 0) dan memiliki nilai yang sangat rendah atau 0 pada semester pertama (Curricular units 1st sem grade) memiliki kecenderungan paling tinggi untuk putus kuliah.
- Performa Model: Model Random Forest Classifier berhasil dikembangkan dengan performa yang sangat baik, terutama pada metrik Recall untuk kelas Dropout, sehingga sangat andal untuk digunakan sebagai jaring pengaman deteksi dini.

## Rekomendasi Action Items
1. Intervensi Finansial Dini: Mengingat faktor tunggakan biaya kuliah sangat dominan terhadap dropout, kampus perlu menawarkan opsi restrukturisasi pembayaran (cicilan) atau program beasiswa darurat bagi mahasiswa yang terdeteksi menunggak di semester awal.
2. Program Mentoring Wajib: Mewajibkan sesi bimbingan konseling akademik intensif bagi mahasiswa yang hasil evaluasi pertengahan Semester 1-nya berada di bawah standar rata-rata.
3. Pemanfaatan Sistem Prediksi: Meminta staf penerimaan mahasiswa baru dan staf akademik untuk secara rutin memasukkan profil mahasiswa ke dalam sistem prediksi Streamlit yang telah dibuat, agar langkah mitigasi bisa dilakukan bahkan sebelum mahasiswa memulai semester keduanya.
