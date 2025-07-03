import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="KKN IDBU 4 - Visualisasi Udang", layout="wide")

# Load logo
logo_undip = Image.open("logoundip.png")
logo_desa = Image.open("logoprapaglor.png")

# Header dengan logo kiri-kanan
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image(logo_undip, width=450)
with col2:
    st.markdown("<h2 style='text-align:center; color:#1f77b4;'>KKN IDBU 4 – DESA PRAPAG LOR</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>KECAMATAN LOSARI, KABUPATEN BREBES</p>", unsafe_allow_html=True)
with col3:
    st.image(logo_desa, width=500)

st.markdown("---")

# Split layout: form input dan deskripsi
input_col, desc_col = st.columns([1, 1])

with input_col:
    st.subheader("📥 Input Data Sampling Udang")
    with st.form("input_form"):
        jumlah1 = st.number_input("Jumlah Udang (Ke-1)", min_value=1, step=1, value=20)
        berat1 = st.text_input("Berat Total (Ke-1) dalam gram", value="300")

        jumlah2 = st.number_input("Jumlah Udang (Ke-2)", min_value=1, step=1, value=20)
        berat2 = st.text_input("Berat Total (Ke-2) dalam gram", value="420")

        jumlah3 = st.number_input("Jumlah Udang (Ke-3)", min_value=1, step=1, value=20)
        berat3 = st.text_input("Berat Total (Ke-3) dalam gram", value="540")

        submitted = st.form_submit_button("📈 Tampilkan Grafik")

with desc_col:
    st.subheader("🧾 Deskripsi Program")
    st.markdown("""
    Program ini merupakan bagian dari kegiatan **KKN IDBU 4** di Desa Prapag Lor.  
    Bertujuan untuk membantu petambak, khususnya **ibu-ibu pascamigran**, dalam
    memahami pertumbuhan **berat rata-rata** dan **biomassa** udang vaname
    selama masa pemeliharaan.

    Data diambil melalui metode **sampling manual setiap 5 hari sekali**, lalu diolah
    menggunakan Python dan ditampilkan dalam bentuk grafik interaktif.

    🧑‍🔬 *Teknologi:* Streamlit, Python, Matplotlib  
    📅 *Periode:* 5 Juli – 21 Juli 2025
    """)

# Proses dan tampilkan grafik
if submitted:
    try:
        berat_total = [
            float(berat1.replace(',', '.')),
            float(berat2.replace(',', '.')),
            float(berat3.replace(',', '.'))
        ]
        jumlah_udang = [jumlah1, jumlah2, jumlah3]
        pengambilan = ['Ke-1', 'Ke-2', 'Ke-3']
        x = np.arange(len(pengambilan))

        # Hitung berat rata-rata
        berat_rata = [bt / ju for bt, ju in zip(berat_total, jumlah_udang)]
        st.success("✅ Data berhasil diproses!")

        # Grafik 1: Berat rata-rata
        fig1, ax1 = plt.subplots()
        ax1.plot(x, berat_rata, 'bo-', label='Berat Rata-rata per Ekor')
        z = np.polyfit(x, berat_rata, 2)
        p = np.poly1d(z)
        x_model = np.linspace(0, 2, 100)
        ax1.plot(x_model, p(x_model), 'r--', label='Kurva Model')
        ax1.set_xticks(x)
        ax1.set_xticklabels(pengambilan)
        ax1.set_xlabel('Pengambilan Data Ke-')
        ax1.set_ylabel('Berat Rata-rata (gram)')
        ax1.set_title('Pertumbuhan Berat Rata-rata Udang')
        ax1.grid(True)
        ax1.legend()
        st.pyplot(fig1)

        # Grafik 2: Biomassa
        biomassa_15 = [w * 15 for w in berat_rata]
        biomassa_30 = [w * 30 for w in berat_rata]
        biomassa_45 = [w * 45 for w in berat_rata]

        fig2, ax2 = plt.subplots()
        ax2.plot(x, biomassa_15, 'g^-', label='15 Ekor')
        ax2.plot(x, biomassa_30, 'bs-', label='30 Ekor')
        ax2.plot(x, biomassa_45, 'ro-', label='45 Ekor')
        ax2.set_xticks(x)
        ax2.set_xticklabels(pengambilan)
        ax2.set_xlabel('Pengambilan Data Ke-')
        ax2.set_ylabel('Biomassa (gram)')
        ax2.set_title('Biomassa Udang Vaname')
        ax2.grid(True)
        ax2.legend()
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"❌ Kesalahan input: {e}")
