import json
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langsmith import Client

load_dotenv()

client = Client()

print("LANGSMITH CONNECTED")
print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
print("TRACING:", os.getenv("LANGCHAIN_TRACING_V2"))


def load_car_data():
    with open("rental_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


cars = load_car_data()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)


prompt_template = PromptTemplate(
    input_variables=["cars", "question"],
    template="""
Anda adalah AI Rental Mobil Assistant yang profesional.

Tugas Anda:
1. Menjawab pertanyaan berdasarkan data mobil yang tersedia.
2. Memahami typo, singkatan, dan bahasa sehari-hari pengguna.
3. Jika pengguna salah ketik, tetap pahami maksudnya.
4. Jika pertanyaan tidak jelas, minta klarifikasi dengan sopan.
5. Jangan mengarang mobil yang tidak ada pada data.
6. Berikan jawaban yang ramah dan profesional.
7. Gunakan bahasa Indonesia.

Data Mobil:

{cars}

Pertanyaan Pengguna:

{question}

Jawaban:
"""
)


def clean_question(question):
    return question.strip().lower()


def generate_answer(question):
    try:

        prompt = prompt_template.format(
            cars=cars,
            question=clean_question(question)
        )

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
        return f"❌ Terjadi kesalahan sistem:\n{str(e)}"