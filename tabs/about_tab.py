import streamlit as st

def display_about_tab():
    """Menampilkan konten tab Tentang."""

    st.header("ℹ️ Tentang IDocspy")

    st.markdown("""
    **IDocspy** adalah aplikasi **Pemrosesan Dokumen Cerdas (Intelligent Document Processing - IDP)** yang dirancang untuk meningkatkan efisiensi interaksi organisasi dengan aset informasinya. Aplikasi ini memanfaatkan kecerdasan buatan (AI) untuk mengotomatisasi ekstraksi teks, analisis konten, dan penemuan informasi, mengubah dokumen statis menjadi sumber pengetahuan yang dinamis dan terkelola. Desain IDocspy mengadopsi prinsip-prinsip yang selaras dengan standar internasional dalam manajemen informasi dan rekod (seperti prinsip dalam ISO 15489), dengan fokus pada penciptaan metadata, keterlacakan proses, dan akses terkontrol, untuk mendukung tata kelola informasi yang baik. Meskipun tidak dimaksudkan sebagai sistem Electronic Document and Records Management System (EDRMS), IDocspy berfungsi sebagai komponen pendukung yang kuat dalam ekosistem manajemen rekod digital.

    ### Kemampuan Inti
    IDocspy meningkatkan alur kerja dokumen melalui fungsi-fungsi utama berikut:
    *   **Manajemen Metadata Rekod:** Mencatat dan mengelola metadata esensial untuk setiap dokumen yang diproses dalam basis data SQLite internal. Metadata yang ditangkap mencakup `filename` (nama tampilan), `base_filename` (identifier unik internal), `processed_at` (cap waktu pemrosesan), `provider` (metode ekstraksi/OCR), `chunk_size`, `chunk_overlap` (parameter segmentasi teks), `keywords` (kata kunci hasil analisis AI, disimpan sebagai JSON), dan `notes` (catatan pengguna). Pencatatan metadata ini mendukung prinsip penciptaan rekod yang andal dan kontekstual.
    *   **Analisis Konten Berbasis AI:** Selama pemrosesan, sistem menganalisis isi dokumen untuk memberikan *saran* klasifikasi, mengekstraksi kata kunci relevan secara otomatis, dan mengidentifikasi potensi indikator sensitivitas data berdasarkan pola konten. Fitur ini berfungsi sebagai alat bantu untuk penilaian awal dan pengorganisasian dokumen.
    *   **Pemrosesan Dokumen Fleksibel:** Mendukung berbagai format input termasuk **PDF, gambar (PNG, JPG, JPEG, TIFF, BMP, WEBP), Microsoft Word (DOCX), Markdown (MD), dan Teks (TXT)**. Menyediakan opsi ekstraksi teks langsung (untuk PDF digital) atau penggunaan layanan OCR terintegrasi (seperti Groq, Google Gemini, Mistral, Pypdf2) untuk dokumen pindaian, yang dapat dikonfigurasi oleh admin. Metrik kualitas teks hasil ekstraksi dihitung untuk memberikan indikasi keandalan proses. Tabel dari dokumen PDF juga diekstraksi dan diintegrasikan untuk kueri AI.
    *   **Penemuan Informasi Hibrida:** Dokumen yang diproses diindeks menggunakan kombinasi **pencarian semantik (FAISS)** dan **pencarian kata kunci (BM25)**. Hasil dari kedua metode ini disatukan menggunakan **Reciprocal Rank Fusion (RRF)** untuk mendapatkan segmen teks yang paling relevan secara kontekstual. Pengguna dapat mengajukan pertanyaan dalam bahasa alami melalui tab Chatbot, dan sistem menyajikan jawaban yang didukung oleh kutipan dari dokumen, lengkap dengan referensi sumber. Fitur pencarian lanjutan seperti HyDE (Hypothetical Document Embeddings) dan re-ranking juga didukung untuk meningkatkan akurasi.
    *   **Modul Kontrol Dokumen (MDR):** Menyediakan tab khusus untuk membantu pengelolaan Master Document Register. Modul ini memungkinkan unggah dokumen dan menggunakan AI (Google Gemini) untuk secara otomatis mengekstraksi metadata kunci yang relevan dengan bidang-bidang MDR, yang kemudian dapat ditinjau, diedit, dan disimpan ke dalam basis data MDR (saat ini disimulasikan).
    *   **Kontrol Administratif:** Akses ke fungsi administratif (melalui login) memungkinkan pengelolaan siklus hidup rekod dalam sistem ini, termasuk pengeditan metadata deskriptif (`filename`, `notes`, `provider`, `keywords`) dan penghapusan rekod melalui tab Database. Tab Admin menyediakan kontrol atas proses unggah, konfigurasi pemrosesan (penyedia OCR, ukuran *chunk*, pemrosesan ulang paksa), dan pengaturan parameter pencarian global (jumlah hasil `k`, ambang batas skor, dll.), mendukung prinsip tata kelola dan kontrol akses.

    ### Fondasi Teknis dan Penanganan Data
    Dibangun dengan Python dan Streamlit, IDocspy menggunakan basis data SQLite untuk manajemen metadata rekod (termasuk data MDR yang disimulasikan) dan FAISS untuk pengindeksan vektor. Aplikasi ini dapat diintegrasikan dengan berbagai penyedia layanan OCR dan model AI (dikonfigurasi via tab Admin). Teks hasil pemrosesan, indeks FAISS, dan berkas terkait disimpan secara lokal di direktori `processed_docs`. Basis data SQLite juga disimpan lokal. Penggunaan layanan cloud untuk OCR atau analisis AI bersifat *opsional dan dapat dikonfigurasi*, memastikan kontrol atas residensi data inti tetap berada di lingkungan pengguna.

    ### Tujuan Penggunaan
    IDocspy dirancang untuk organisasi atau unit kerja yang bertujuan untuk:
    - Mempercepat pemrosesan, pemahaman, dan analisis koleksi dokumen digital.
    - Menerapkan metode pencarian dan kueri konten dokumen yang efisien dan kontekstual.
    - Mengotomatisasi langkah awal dalam analisis dokumen, seperti ekstraksi kata kunci dan pemberian saran klasifikasi, sebagai input potensial untuk sistem EDRMS.
    - Membantu proses ekstraksi metadata untuk Master Document Register (MDR) menggunakan bantuan AI.
    - Menyediakan data terstruktur (metadata pemrosesan dan analisis) yang dapat mendukung proses klasifikasi, penilaian, dan penelusuran rekod dalam kerangka kerja EDRMS yang lebih luas, meningkatkan *findability* dan *traceability*.
    """)
    
    st.subheader("⚠️ Penting")
    st.info("""
        * Untuk implementasi dalam lingkungan produksi, IDocspy memerlukan peningkatan infrastruktur
        * Berminat membangun solusi serupa untuk manajemen dokumen di organisasi Anda? Hubungi pengembang.
    """)
    # Versi dan detail teknis
    st.markdown("---")
    st.caption("IDocspy, Built by Adnuri Mohamidi with help from AI :orange_heart:", help="cyberariani@gmail.com")
