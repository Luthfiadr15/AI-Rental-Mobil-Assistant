import json
import os

from functools import lru_cache
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langsmith import Client

# ==================================
# LOAD ENV
# ==================================

load_dotenv()

client = Client()

print("LANGSMITH CONNECTED")
print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
print("TRACING:", os.getenv("LANGCHAIN_TRACING_V2"))

# ==================================
# LOAD DATA
# ==================================

def load_car_data():

    with open(
        "rental_data.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


cars = load_car_data()

# ==================================
# GEMINI MODEL
# ==================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

# ==================================
# PROMPT
# ==================================

prompt_template = PromptTemplate(
    input_variables=[
        "cars",
        "question"
    ],
    template="""
Anda adalah AI Rental Mobil Assistant.

Aturan:
1. Jawab hanya berdasarkan data mobil yang tersedia.
2. Pahami typo dan bahasa sehari-hari pengguna.
3. Jangan mengarang data.
4. Gunakan bahasa Indonesia yang ramah.
5. Berikan rekomendasi terbaik jika memungkinkan.
6. Jawaban maksimal 150 kata.

Data Mobil:

{cars}

Pertanyaan:

{question}

Jawaban:
"""
)

# ==================================
# CLEAN QUESTION
# ==================================

def clean_question(question):

    return question.strip().lower()

# ==================================
# GENERATE ANSWER
# ==================================

@lru_cache(maxsize=100)
def generate_answer(question):

    try:

        question = clean_question(question)

        # ==================================
        # ROMBONGAN
        # ==================================

        if any(
            x in question
            for x in [
                "10 orang",
                "15 orang",
                "rombongan",
                "keluarga besar",
                "banyak orang"
            ]
        ):

            car = max(
                cars,
                key=lambda x: x["kapasitas"]
            )

            return (
                f"🚗 Saya merekomendasikan {car['nama']}\n\n"
                f"💰 Harga: Rp {car['harga']:,}/hari\n"
                f"👥 Kapasitas: {car['kapasitas']} orang\n"
                f"⚙️ Transmisi: {car['transmisi']}"
            )

        # ==================================
        # TERMURAH
        # ==================================

        if any(
            x in question
            for x in [
                "murah",
                "termurah",
                "budget",
                "hemat"
            ]
        ):

            car = min(
                cars,
                key=lambda x: x["harga"]
            )

            return (
                f"🚗 Mobil termurah adalah {car['nama']}\n\n"
                f"💰 Harga: Rp {car['harga']:,}/hari\n"
                f"👥 Kapasitas: {car['kapasitas']} orang\n"
                f"⚙️ Transmisi: {car['transmisi']}"
            )

        # ==================================
        # TERMAHAL
        # ==================================

        if any(
            x in question
            for x in [
                "mahal",
                "termahal",
                "premium"
            ]
        ):

            car = max(
                cars,
                key=lambda x: x["harga"]
            )

            return (
                f"🚗 Mobil premium adalah {car['nama']}\n\n"
                f"💰 Harga: Rp {car['harga']:,}/hari\n"
                f"👥 Kapasitas: {car['kapasitas']} orang\n"
                f"⚙️ Transmisi: {car['transmisi']}"
            )

        # ==================================
        # MATIC
        # ==================================

        if any(
            x in question
            for x in [
                "matic",
                "automatic",
                "otomatis"
            ]
        ):

            for car in cars:

                if car["transmisi"].lower() == "automatic":

                    return (
                        f"🚗 Saya merekomendasikan {car['nama']}\n\n"
                        f"💰 Harga: Rp {car['harga']:,}/hari\n"
                        f"👥 Kapasitas: {car['kapasitas']} orang\n"
                        f"⚙️ Transmisi: {car['transmisi']}"
                    )

        # ==================================
        # MANUAL
        # ==================================

        if "manual" in question:

            for car in cars:

                if car["transmisi"].lower() == "manual":

                    return (
                        f"🚗 Mobil manual yang tersedia adalah {car['nama']}\n\n"
                        f"💰 Harga: Rp {car['harga']:,}/hari\n"
                        f"👥 Kapasitas: {car['kapasitas']} orang\n"
                        f"⚙️ Transmisi: {car['transmisi']}"
                    )

        # ==================================
        # CARI BERDASARKAN NAMA MOBIL
        # ==================================

        for car in cars:

            if car["nama"].lower() in question:

                return (
                    f"🚗 {car['nama']}\n\n"
                    f"💰 Harga: Rp {car['harga']:,}/hari\n"
                    f"👥 Kapasitas: {car['kapasitas']} orang\n"
                    f"⚙️ Transmisi: {car['transmisi']}"
                )

        # ==================================
        # GEMINI FALLBACK
        # ==================================

        prompt = prompt_template.format(
            cars=cars,
            question=question
        )

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return (
            "❌ Terjadi kesalahan sistem:\n"
            f"{str(e)}"
        )