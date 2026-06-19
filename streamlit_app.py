import pandas as pd
import plotly.express as px
import streamlit as st
import json
import base64
import datetime

from graph import graph

# ==================================
# CONFIG
# ==================================

st.set_page_config(
    page_title="AI Rental Mobil Assistant",
    page_icon="🚗",
    layout="wide"
)

# ==================================
# IMAGE
# ==================================

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

hero_img = get_base64("assets/hero.jpg")

# ==================================
# CSS
# ==================================

st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background: #020617;
}}

section[data-testid="stSidebar"] {{
    background: #0f172a;
    border-right: 1px solid rgba(255,255,255,0.08);
}}

.main .block-container {{
    padding-top: 2rem;
}}

.hero {{
    background:
        linear-gradient(
            rgba(37,99,235,0.75),
            rgba(29,78,216,0.75)
        ),
        url("data:image/jpg;base64,{hero_img}");

    background-size: cover;
    background-position: center;
    border-radius: 25px;
    padding: 120px 50px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
    box-shadow: 0 10px 40px rgba(37,99,235,0.25);
}}

.badge {{
    display: inline-block;
    padding: 10px 18px;
    margin: 6px;
    border-radius: 999px;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    color: white;
    font-weight: 500;
}}

.ai-card {{
    background: white;
    color: black;
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}}

.footer {{
    text-align: center;
    color: white;
    padding: 40px;
}}

h1, h2, h3 {{
    color: white;
}}

[data-testid="stMetric"] {{
    background: #0f172a;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 18px;
}}

[data-testid="stMetricValue"] {{
    color: white;
}}

[data-testid="stMetricLabel"] {{
    color: #94a3b8;
}}

[data-testid="stVerticalBlockBorderWrapper"] {{
    background: #0f172a;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 15px;
    min-height: 520px;
    transition: 0.3s;
}}

[data-testid="stVerticalBlockBorderWrapper"]:hover {{
    border: 1px solid #3b82f6;
    transform: translateY(-3px);
}}

[data-testid="stImage"] img {{
    border-radius: 15px;
}}

button {{
    border-radius: 12px !important;
}}

.stButton > button {{
    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );
    color: white;
    border: none;
    font-weight: bold;
}}

.stButton > button:hover {{
    background: linear-gradient(
        135deg,
        #1d4ed8,
        #2563eb
    );
}}

input {{
    border-radius: 12px !important;
}}

hr {{
    border-color: rgba(255,255,255,0.1);
}}

</style>
""", unsafe_allow_html=True)

# ==================================
# DATA
# ==================================

with open(
    "rental_data.json",
    "r",
    encoding="utf-8"
) as file:

    cars = json.load(file)

# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.markdown("""
    <h2 style='text-align:center; color:white;'>
    🚗 Rental AI
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🧠 Teknologi")

    st.markdown("""
    ✅ LangChain<br>
    ✅ LangGraph<br>
    ✅ LangSmith<br>
    ✅ Gemini 2.5 Flash
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📋 Fitur")

    st.markdown("""
    🚗 Rekomendasi Mobil AI<br>
    👨‍👩‍👧‍👦 Analisis Kapasitas<br>
    💰 Analisis Budget<br>
    ⚙️ Analisis Transmisi<br>
    🤖 Natural Language Query
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎓 Identitas")

    st.markdown("""
    Universitas Islam Riau<br>
    Teknik Informatika<br>
    Mata Kuliah NLP
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.caption("AI Rental Mobil Assistant v1.0")
# ==================================
# HERO
# ==================================

st.markdown("""
<div class="hero">

<h1 style="font-size:72px;">
🚗 AI Rental Mobil Assistant
</h1>

<h2>
Temukan Mobil Terbaik Dengan Bantuan AI
</h2>

<p>
Menggunakan LangChain, LangGraph,
LangSmith dan Gemini AI
</p>

<br>

<span class="badge">✅ LangChain</span>

<span class="badge">✅ LangGraph</span>

<span class="badge">✅ LangSmith</span>

<span class="badge">✅ Gemini AI</span>

</div>
""", unsafe_allow_html=True)

# ==================================
# CHAT HISTORY
# ==================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# SEARCH
# ==================================

st.subheader("🤖 Tanya AI Rental Assistant")

question = st.text_input(
    "",
    placeholder="🚗 Contoh: mobil untuk 10 orang atau budget 500rb"
)

if st.button(
    "🚀 Cari Rekomendasi",
    use_container_width=True
):

    if question.strip():

        with st.spinner(
            "AI sedang menganalisis kebutuhan Anda..."
        ):

            result = graph.invoke(
                {
                    "question": question
                }
            )

        # Simpan ke Riwayat
        st.session_state.history.append(
            {
                "question": question,
                "answer": result["answer"]
            }
        )

        # Tampilkan Hasil AI
        st.markdown("### 🤖 Rekomendasi AI")

        st.success(
            result["answer"]
        )

        # Download Hasil
        st.download_button(
            label="📥 Download Hasil AI",
            data=result["answer"],
            file_name=f"hasil_ai_{datetime.date.today()}.txt",
            mime="text/plain",
            use_container_width=True
        )

    else:

        st.warning(
            "Silakan masukkan pertanyaan terlebih dahulu."
        )

# ==================================
# RIWAYAT CHAT
# ==================================

if len(st.session_state.history) > 0:

    st.markdown("---")
    st.subheader("📝 Riwayat Konsultasi")

    if st.button(
        "🗑️ Hapus Riwayat",
        use_container_width=True
    ):

        st.session_state.history = []
        st.rerun()

    for item in reversed(
        st.session_state.history
    ):

        with st.expander(
            f"❓ {item['question']}"
        ):

            st.write(
                item["answer"]
            )

# ==================================
# RIWAYAT CHAT
# ==================================

if len(st.session_state.history) > 0:

    st.markdown("---")
    st.subheader("📝 Riwayat Konsultasi")

    if st.button("🗑️ Hapus Riwayat"):

        st.session_state.history = []

        st.rerun()

    for item in reversed(st.session_state.history):

        with st.expander(
            f"❓ {item['question']}"
        ):

            st.write(
                item["answer"]
            )

# ==================================
# STATISTIK
# ==================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "🚘 Total Mobil",
        len(cars)
    )

with col2:

    automatic = len([
        c for c in cars
        if c["transmisi"].lower() == "automatic"
    ])

    st.metric(
        "⚙️ Automatic",
        automatic
    )

with col3:

    max_capacity = max(
        c["kapasitas"]
        for c in cars
    )

    st.metric(
        "👥 Kapasitas Maks",
        max_capacity
    )


st.markdown("---")
st.subheader("🔍 Filter Mobil")

col1, col2 = st.columns(2)

with col1:
    budget = st.number_input(
        "Budget Maksimal (Rp)",
        min_value=0,
        value=1500000,
        step=50000
    )

with col2:
    kapasitas = st.selectbox(
        "Jumlah Penumpang",
        [0, 5, 7, 15]
    )
    
# ==================================
# GRAFIK HARGA MOBIL
# ==================================

st.markdown("---")
st.subheader("📊 Perbandingan Harga Mobil")

df = pd.DataFrame(cars)

fig = px.bar(
    df,
    x="nama",
    y="harga",
    text="harga",
    title="Harga Sewa Mobil per Hari"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")
st.subheader("📊 Distribusi Transmisi")

df = pd.DataFrame(cars)

fig2 = px.pie(
    df,
    names="transmisi",
    title="Distribusi Jenis Transmisi"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)   

# ==================================
# STATISTIK DATASET
# ==================================

st.markdown("---")
st.subheader("📈 Statistik Dataset")

harga_termurah = min(
    c["harga"] for c in cars
)

harga_termahal = max(
    c["harga"] for c in cars
)

rata_rata = sum(
    c["harga"] for c in cars
) / len(cars)

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        f"💰 Termurah: Rp {harga_termurah:,.0f}"
    )

with c2:
    st.warning(
        f"📊 Rata-rata: Rp {rata_rata:,.0f}"
    )

with c3:
    st.error(
        f"🔥 Termahal: Rp {harga_termahal:,.0f}"
    )
    
    
# ==================================
# FILTER MOBIL
# ==================================

filtered_cars = []

for car in cars:

    budget_ok = car["harga"] <= budget

    kapasitas_ok = (
        kapasitas == 0
        or car["kapasitas"] >= kapasitas
    )

    if budget_ok and kapasitas_ok:

        filtered_cars.append(car)

st.success(
    f"Ditemukan {len(filtered_cars)} mobil sesuai filter"
)

if len(filtered_cars) > 0:

    rekomendasi = min(
        filtered_cars,
        key=lambda x: x["harga"]
    )

    st.info(
        f"""
🏆 Rekomendasi Terbaik

🚗 {rekomendasi['nama']}

💰 Rp {rekomendasi['harga']:,}/hari

👥 {rekomendasi['kapasitas']} Penumpang

⚙️ {rekomendasi['transmisi']}
"""
    )

if len(filtered_cars) > 0:

    rekomendasi = min(
        filtered_cars,
        key=lambda x: x["harga"]
    )

    st.info(
        f"""
🏆 Rekomendasi Terbaik

🚗 {rekomendasi['nama']}

💰 Rp {rekomendasi['harga']:,}/hari

👥 {rekomendasi['kapasitas']} Penumpang

⚙️ {rekomendasi['transmisi']}
"""
    )

# ==================================
# GALERI MOBIL PREMIUM
# ==================================

st.markdown("---")
st.subheader("🚘 Mobil Tersedia")

car_images = {
    "Honda Brio": "assets/brio.jpg",
    "Toyota Avanza": "assets/avanza.jpg",
    "Toyota Innova": "assets/innova.jpg",
    "Toyota Hiace": "assets/hiace.jpg",
    "Mitsubishi Pajero": "assets/pajero.jpg"
}

col1, col2, col3 = st.columns(3)

for i, car in enumerate(filtered_cars):

    image_path = car_images.get(
        car["nama"],
        "assets/hero.jpg"
    )

    current_col = [col1, col2, col3][i % 3]

    with current_col:

        with st.container(border=True):

            st.image(
                image_path,
                use_container_width=True
            )

            st.markdown(
                f"""
### 🚗 {car['nama']}

💰 **Rp {car['harga']:,} / Hari**

👥 **{car['kapasitas']} Penumpang**

⚙️ **{car['transmisi']}**
"""
            )

            if st.button(
                "Lihat Detail",
                key=f"detail_{i}",
                use_container_width=True
            ):

                st.info(
                    f"""
🚗 {car['nama']}

💰 Harga : Rp {car['harga']:,}/hari

👥 Kapasitas : {car['kapasitas']} orang

⚙️ Transmisi : {car['transmisi']}
"""
                )

st.markdown("---")

with st.expander("ℹ️ Tentang Project"):

    st.write("""
AI Rental Mobil Assistant merupakan sistem rekomendasi
mobil berbasis Natural Language Processing (NLP).

Teknologi yang digunakan:

- LangChain
- LangGraph
- LangSmith
- Gemini AI
- Streamlit

Fitur:

- Analisis kebutuhan pengguna
- Filter mobil berdasarkan budget
- Filter kapasitas penumpang
- Visualisasi data
- Riwayat konsultasi
- Download hasil rekomendasi
""")

# ==================================
# FOOTER
# ==================================

st.markdown("""
<div class="footer">

<hr>

<h4>
AI Rental Mobil Assistant
</h4>

<p>
LangChain • LangGraph • LangSmith • Gemini AI
</p>

</div>
""", unsafe_allow_html=True)