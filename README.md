# 🧠 Face Recognition Platform with Real-Time AI Q&A using RAG and Azure OpenAI

This full-stack project integrates **face recognition**, **RAG-based Q&A (LangChain + FAISS + Azure OpenAI)**, and **real-time chat** using **Flask**, **React.js**, **Node.js**, and **MongoDB**.

---

## 🌐 Live Features

- 🧑‍💻 Register and recognize faces from webcam
- 🤖 Real-time question answering via LangChain + FAISS + Azure OpenAI
- 🧠 Uses RAG (Retrieval-Augmented Generation)
- 🔒 MongoDB for persistent face embedding storage
- 🔌 WebSocket server for real-time chat between user and AI

---

## 📁 Project Structure

face-recognition-rag-platform/
│
├── backend/
│ ├── app.py # Flask entry point
│ ├── api/
│ │ └── face_routes.py # Routes for face registration/recognition
│ ├── services/
│ │ └── db_service.py # MongoDB interaction
│ ├── rag_engine.py # LangChain + FAISS + Azure OpenAI integration
│ ├── config.py # Config handling (env loading)
│ └── requirements.txt # Python dependencies
│
├── node-server/
│ └── server.js # Node.js WebSocket bridge
│
├── frontend/
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── components/
│ │ │ ├── Register.js
│ │ │ ├── LiveRecognition.js
│ │ │ └── ChatWidget.js
│ │ ├── App.js
│ │ └── index.js
│ └── package.json
│
├── .env # API keys and Mongo URI (excluded from version control)
├── README.md
└── architecture.png # System diagram


---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/face-recognition-rag-platform.git
cd face-recognition-rag-platform

2️⃣ Setup Backend (Flask)

cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

🔐 Create .env in backend/envCopyEdit

MONGO_URI=mongodb+srv://<user>:<pass>@cluster.mongodb.net/?retryWrites=true&w=majority
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment
AZURE_OPENAI_MODEL=gpt-35-turbo

3️⃣ Setup Node WebSocket Server

cd ../node-server
npm install
node server.js

4️⃣ Setup Frontend (React.js)

cd ../frontend
npm install
npm start

🛠️ Tech Stack

| Layer     | Tools                                     |
| --------- | ----------------------------------------- |
| Frontend  | React.js, HTML, CSS, JavaScript           |
| Backend   | Flask (Python)                            |
| AI Engine | LangChain + FAISS + Azure OpenAI (GPT)    |
| Database  | MongoDB Atlas                             |
| Realtime  | Node.js WebSocket                         |
| DevOps    | GitHub, GitHub Student Pack (API credits) |


💡 RAG Engine

    -Embeds documents using OpenAIEmbeddings

    -Stores vectors in FAISS

    -Uses LangChain RetrievalQA for question-answering

    -Powered by Azure OpenAI GPT models

🧠 How It Works
    -📸 Face captured via webcam

    -🔐 Face embeddings stored/retrieved from MongoDB

    -❓ User asks a question

    -🔍 RAG retrieves documents using FAISS

    -🧠 Azure OpenAI generates response

    -💬 Real-time WebSocket sends back answer

    -🧑‍🎓 GitHub Student Pack Users
You can get free Azure credits and OpenAI API keys via:

https://education.github.com/pack

    -Create a Microsoft Azure for Students account

    -Use the credits for deploying your own GPT model with Azure OpenAI Studio