import streamlit as st
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()
HF_TOKEN = os.getenv("hf")

if HF_TOKEN is None:
    st.error(" Hugging Face token not found. Check your .env file.")
    st.stop()

os.environ["HF_TOKEN"] = HF_TOKEN

st.set_page_config(
    page_title="AI Chatbot Mentor",
    page_icon="🤖",
    layout="centered"
)

MODULES = {
    "Python": "🐍",
    "SQL": "🗄️",
    "Power BI": "📊",
    "Exploratory Data Analysis (EDA)": "📈",
    "Machine Learning (ML)": "🤖",
    "Deep Learning (DL)": "🧠",
    "Generative AI (Gen AI)": "✨",
    "Agentic AI": "🧩",
}

MODULE_KEYWORDS = {
    "Python": ["python", "list", "tuple", "dict", "loop", "function", "class"],
    "SQL": ["sql", "select", "join", "where", "group by", "table", "database"],
    "Power BI": ["power bi", "powerbi", "dax", "pbix", "dashboard", "report", "visual"],
    "Exploratory Data Analysis (EDA)": ["eda", "outlier", "distribution", "correlation"],
    "Machine Learning (ML)": ["machine learning", "ml", "supervised", "unsupervised", "model"],
    "Deep Learning (DL)": ["deep learning", "neural network", "cnn", "rnn", "backpropagation"],
    "Generative AI (Gen AI)": ["generative", "llm", "prompt", "transformer"],
    "Agentic AI": ["agent", "tool", "planner", "memory", "autonomous"],
}

BLOCK_MSG = (
    "Sorry, I don’t know about this question. "
    "Please ask something related to the selected module."
)

def is_relevant(question: str, module: str) -> bool:
    q = question.lower().strip()
    return any(k in q for k in MODULE_KEYWORDS[module])

st.sidebar.title("🤖 AI Chatbot Mentor")
st.sidebar.write("Select a learning module and ask questions only from that topic.")

module = st.sidebar.selectbox(
    "📚 Choose Module",
    list(MODULES.keys())
)

if st.sidebar.button("🆕 New Chat"):
    st.session_state.messages = []
    st.session_state.active_module = module
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Hugging Face + LangChain")

icon = MODULES[module]


SYSTEM_PROMPT = f"""
You are an expert mentor ONLY for {module}.

STRICT RULES:
- Answer ONLY questions related to {module}
- If the question is NOT related, reply EXACTLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."

ANSWER STYLE:
- Explain clearly for a beginner
- Use simple language
- Give a short definition
- Give 1 small example if applicable
- Do NOT mention other domains
"""

if "active_module" not in st.session_state or st.session_state.active_module != module:
    st.session_state.active_module = module
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

if "model" not in st.session_state:
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        temperature=0.3,
        max_new_tokens=800,
    )
    st.session_state.model = ChatHuggingFace(llm=llm)

st.markdown(
    f"""
    <h1 style='text-align:center;'>👋 AI Chatbot Mentor</h1>
    <h3 style='text-align:center;'>{icon} {module} Mentor</h3>
    <hr>
    """,
    unsafe_allow_html=True
)

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input(f"Ask a {module} question")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    if not is_relevant(prompt, module):
        with st.chat_message("assistant"):
            st.write(BLOCK_MSG)

        st.session_state.messages.append(
            {"role": "assistant", "content": BLOCK_MSG}
        )

    else:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        response = st.session_state.model.invoke(
            st.session_state.messages
        )

        answer = response.content.strip()

        if len(answer) < 50:
            answer += "\n\n(Ask a more specific question for deeper explanation.)"

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

if len(st.session_state.messages) > 1:
    chat_text = ""
    for m in st.session_state.messages[1:]:
        chat_text += f"{m['role'].upper()}:\n{m['content']}\n\n"

    st.download_button(
        "📥 Download Conversation",
        chat_text,
        file_name=f"{module}_chat.txt",
        mime="text/plain"
    )