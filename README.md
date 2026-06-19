# 🚗 AI Rental Mobil Assistant

AI Rental Mobil Assistant adalah aplikasi rekomendasi mobil berbasis Artificial Intelligence (AI) dan Natural Language Processing (NLP) yang membantu pengguna menemukan mobil rental sesuai kebutuhan berdasarkan kapasitas penumpang, budget, dan preferensi kendaraan.

Project ini dikembangkan sebagai tugas UAS Mata Kuliah Natural Language Processing (NLP), Program Studi Teknik Informatika, Universitas Islam Riau.

---

## ✨ Features

* 🤖 AI Car Recommendation
* 💬 Natural Language Query
* 👥 Capacity Analysis
* 💰 Budget Analysis
* 🚗 Car Filtering
* 📊 Data Visualization
* 📝 Consultation History
* 📥 Download Recommendation Result
* 📈 Dataset Statistics
* 🎨 Interactive Streamlit Dashboard

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### AI & NLP

* LangChain
* LangGraph
* LangSmith
* Google Gemini AI

### Data Processing

* Pandas
* Plotly

### Programming Language

* Python

---

## 📂 Project Structure

```text
AI-Rental-Mobil-Assistant/
│
├── assets/
│   ├── hero.jpg
│   ├── avanza.jpg
│   ├── brio.jpg
│   ├── innova.jpg
│   ├── hiace.jpg
│   └── pajero.jpg
│
├── screenshots/
│
├── app.py
├── chatbot.py
├── graph.py
├── streamlit_app.py
├── rental_data.json
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/USERNAME/AI-Rental-Mobil-Assistant.git
cd AI-Rental-Mobil-Assistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create file `.env`

```env
GOOGLE_API_KEY=YOUR_API_KEY
LANGCHAIN_API_KEY=YOUR_LANGSMITH_KEY
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=AI-Rental-Mobil-Assistant
```

---

## ▶️ Run Application

```bash
streamlit run streamlit_app.py
```

Application will run at:

```text
http://localhost:8501
```

---

## 📊 Main Features Demonstration

* AI recommendation based on user needs.
* Vehicle filtering by budget and passenger capacity.
* Rental vehicle statistics visualization.
* Consultation history storage.
* Recommendation result download.
* Interactive dashboard with Streamlit.

---

## 🎓 Academic Information

**Course:** Natural Language Processing (NLP)

**Study Program:** Informatics Engineering

**University:** Universitas Islam Riau

---

## 👨‍💻 Developer

Muhammad Luthfi Adrian

Teknik Informatika

Universitas Islam Riau

2026
