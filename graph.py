from typing import TypedDict

from chatbot import generate_answer

from langgraph.graph import StateGraph


class RentalState(TypedDict):
    question: str
    answer: str


def process_question(state):

    answer = generate_answer(
        state["question"]
    )

    return {
        "answer": answer
    }


builder = StateGraph(RentalState)

builder.add_node(
    "rental_assistant",
    process_question
)

builder.set_entry_point(
    "rental_assistant"
)

builder.set_finish_point(
    "rental_assistant"
)

graph = builder.compile()