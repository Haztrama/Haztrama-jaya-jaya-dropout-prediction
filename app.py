import streamlit as st
import pandas as pd
import joblib

# Konfigurasi Halaman
st.set_page_config(
    page_title="Jaya Jaya Institut - Dropout Prediction",
    page_icon="🎓",
    layout="centered"
)

# Load Model
@st.cache_resource
def load_model():
    # Pastikan path ini sesuai dengan lokasi model Anda
    # Jika model ditaruh di dalam folder 'model', gunakan 'model/model_rf.joblib'
    return joblib.load('model_rf.joblib')

model = load_model()

# Header Aplikasi
st.title("🎓 Sistem Prediksi Dropout Mahasiswa")
st.markdown("""
Aplikasi ini dirancang untuk mendeteksi dini apakah seorang mahasiswa berisiko putus kuliah (*dropout*). 
Silakan masukkan data akademik dan finansial mahasiswa pada form di bawah ini.
""")

st.divider()

# Membuat Layout Form Input
st.subheader("📝 Form Data Mahasiswa")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Status Finansial**")
    tuition_up_to_date = st.selectbox(
        "Apakah biaya kuliah (UKT) lunas/up-to-date?",
        options=[1, 0],
        format_func=lambda x: "Ya (Lunas)" if x == 1 else "Tidak (Menunggak)"
    )
    debtor = st.selectbox(
        "Apakah mahasiswa memiliki hutang?",
        options=[0, 1],
        format_func=lambda x: "Tidak" if x == 0 else "Ya"
    )
    scholarship = st.selectbox(
        "Apakah mahasiswa penerima beasiswa?",
        options=[0, 1],
        format_func=lambda x: "Tidak" if x == 0 else "Ya"
    )

with col2:
    st.markdown("**Performa Akademik (Semester 1)**")
    sem1_grade = st.slider(
        "Rata-rata Nilai Semester 1", 
        min_value=0.0, max_value=20.0, value=12.0, step=0.1
    )
    sem1_approved = st.number_input(
        "Jumlah Mata Kuliah Lulus (Semester 1)", 
        min_value=0, max_value=20, value=5
    )
    age = st.number_input(
        "Usia saat mendaftar", 
        min_value=15, max_value=60, value=19
    )

# Tombol Prediksi
if st.button("🔍 Deteksi Risiko Dropout", use_container_width=True):
    # Menyusun data input sesuai dengan 36 kolom yang diharapkan oleh model
    # Kita menggunakan nilai default (median/modus) untuk fitur yang disembunyikan dari UI
    input_data = {
        'Marital_status': 1,
        'Application_mode': 1,
        'Application_order': 1,
        'Course': 9085,
        'Daytime_evening_attendance': 1,
        'Previous_qualification': 1,
        'Previous_qualification_grade': 133.0,
        'Nacionality': 1,
        'Mothers_qualification': 1,
        'Fathers_qualification': 1,
        'Mothers_occupation': 1,
        'Fathers_occupation': 1,
        'Admission_grade': 127.0,
        'Displaced': 1,
        'Educational_special_needs': 0,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_up_to_date,
        'Gender': 0,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 8,
        'Curricular_units_1st_sem_approved': sem1_approved,
        'Curricular_units_1st_sem_grade': sem1_grade,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 8,
        'Curricular_units_2nd_sem_approved': sem1_approved, # Asumsi sama dengan sem 1
        'Curricular_units_2nd_sem_grade': sem1_grade, # Asumsi sama dengan sem 1
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 11.1,
        'Inflation_rate': 0.6,
        'GDP': 0.32
    }

    # Mengubah dictionary menjadi DataFrame satu baris
    df_input = pd.DataFrame([input_data])

    # Melakukan Prediksi
    prediction = model.predict(df_input)

    st.divider()
    st.subheader("📊 Hasil Prediksi")

    # Menampilkan hasil dengan warna yang sesuai
    if prediction[0] == 1:
        st.error("⚠️ **BERISIKO DROPOUT**")
        st.markdown("""
        **Rekomendasi Tindakan:**
        Mahasiswa ini terdeteksi memiliki risiko tinggi untuk putus kuliah. 
        Segera jadwalkan sesi bimbingan konseling akademik dan periksa kembali kendala finansial yang mungkin dialami mahasiswa.
        """)
    else:
        st.success("✅ **AMAN (BERPOTENSI LULUS)**")
        st.markdown("Mahasiswa ini diprediksi akan melanjutkan studi dan lulus dengan baik. Tetap pantau perkembangan akademiknya di semester berikutnya.")
