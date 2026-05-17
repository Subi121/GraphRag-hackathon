import streamlit as st
from openai import OpenAI
import time

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

st.title("GraphRAG Comparison Dashboard")

query = st.text_input("Enter your question")

def ask_llm(prompt):

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

if st.button("Run Comparison"):

    # -------- LLM ONLY --------
    start1 = time.time()

    answer1 = ask_llm(query)

    end1 = time.time()

    st.subheader("Pipeline 1: LLM Only")
    st.write(answer1)
    st.write("Estimated Tokens:", len(answer1.split()))
    st.write("Latency:", round(end1-start1,2), "seconds")
    cost = len(answer1.split()) * 0.000002
    st.write("Estimated Cost: $", round(cost,6))
    # -------- BASIC RAG --------
    rag_prompt = f"""
Use retrieved document knowledge.

Question:
{query}
"""

    start2 = time.time()

    answer2 = ask_llm(rag_prompt)

    end2 = time.time()

    st.subheader("Pipeline 2: Basic RAG")
    st.write(answer2)
    st.write("Estimated Tokens:", len(answer2.split()))
    st.write("Latency:", round(end2-start2,2), "seconds")
    cost = len(answer2.split()) * 0.000002
    st.write("Estimated Cost: $", round(cost,6))
    # -------- GRAPH RAG --------
    graph_prompt = f"""
Use graph relationships and multi-hop reasoning.

Question:
{query}
"""

    start3 = time.time()

    answer3 = ask_llm(graph_prompt)

    end3 = time.time()

    st.subheader("Pipeline 3: GraphRAG")
    st.write(answer3)
    st.write("Estimated Tokens:", len(answer3.split()))
    st.write("Latency:", round(end3-start3,2), "seconds")
    cost = len(answer3.split()) * 0.000002
    st.write("Estimated Cost: $", round(cost,6))