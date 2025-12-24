🤖 AI Chatbot Mentor

An AI-powered learning mentor built with Streamlit, LangChain, and Hugging Face LLMs that provides module-specific guidance for learners in Data Analytics and AI domains.
The chatbot strictly answers questions only from the selected topic, ensuring focused and distraction-free learning.

🚀 Features

📚 Module-Based Learning

Python

SQL

Power BI

Exploratory Data Analysis (EDA)

Machine Learning

Deep Learning

Generative AI

Agentic AI

🔒 Strict Topic Guardrails

Blocks unrelated questions

Enforces module-specific responses using keyword filtering + system prompts

💬 Interactive Chat Interface

Streamlit chat UI

Session-based conversation memory

Reset chat on module change

📥 Download Chat History

Export conversations as .txt files for revision

🧠 Beginner-Friendly Responses

Simple explanations

Short definitions

Small examples when applicable

🛠️ Tech Stack

Frontend: Streamlit

LLM Framework: LangChain

Model Provider: Hugging Face

Model Used: DeepSeek-R1-Distill-Qwen-1.5B

Language: Python

📂 Project Structure
├── app.py               # Main Streamlit application
├── .env                 # Hugging Face API token
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

🔑 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-chatbot-mentor.git
cd ai-chatbot-mentor

2️⃣ Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Hugging Face Token

Create a .env file:

hf=your_huggingface_token_here


Get your token from 👉 https://huggingface.co/settings/tokens

▶️ Run the Application
streamlit run app.py

📸 Application Preview

Select a learning module from the sidebar

Ask questions related only to that module

Download the chat for offline learning

🎯 Use Cases

📘 Beginners learning Python / SQL / Data Analytics

🎓 Students revising AI concepts

🧪 Practicing ML, DL, and GenAI fundamentals

💼 Portfolio project for Data Analyst / AI roles

🧩 Future Enhancements

Difficulty levels (Beginner / Intermediate / Advanced)

User authentication

Chat history persistence (database)

Voice-based interaction

Multiple model support

🙌 Acknowledgements

Streamlit

LangChain

Hugging Face

DeepSeek AI Models

📌 Author

Suddala Srikar
Aspiring Data Analyst | AI Enthusiast

🔗 Feel free to connect and contribute!
