import time

from graph import graph

print("=" * 60)
print("🚗 AI RENTAL MOBIL ASSISTANT")
print("LangChain • LangGraph • LangSmith")
print("=" * 60)

while True:

    question = input("\n🚗 Pertanyaan Anda : ")

    if not question.strip():
        print("⚠️ Silakan masukkan pertanyaan terlebih dahulu.")
        continue

    if question.lower() == "exit":
        print("\n👋 Terima kasih telah menggunakan AI Rental Mobil Assistant.")
        break

    try:
        start = time.time()

        result = graph.invoke(
            {
                "question": question
            }
        )

        end = time.time()

        print("\n🤖 Jawaban AI:")
        print(result["answer"])

        print(
            f"\n⏱️ Waktu respon: {end-start:.2f} detik"
        )

    except Exception as e:
        print(
            f"\n❌ Terjadi kesalahan:\n{str(e)}"
        )