# 🧠 Face Recognition Platform with Real-Time AI Q&A using RAG and OpenRouter.ai

This full-stack project integrates **face recognition**, **RAG-based Q&A (LangChain + FAISS + OpenRouter.ai)**, and **real-time chat** using **Flask**, **React.js**, **Node.js**, and **MongoDB**.

---

## 🌐 Live Features

- 🧑‍💻 Register and recognize faces from webcam
- 🤖 Real-time question answering via LangChain + FAISS + OpenRouter.ai
- 🧠 Uses RAG (Retrieval-Augmented Generation)
- 🔒 MongoDB for persistent face embedding storage
- 🔌 WebSocket server for real-time chat between user and AI

---

## 📁 Project Structure

📁 face-recognition-rag-platform
├── 📁 backend                          # Flask backend
│   ├── 📝 app.py                       # Flask entry point
│   ├── 📝 recognition_api.py          # Main API for face recognition and RAG calls
│   ├── 📁 api
│   │   ├── 📝 face_routes.py          # Routes for face registration/recognition
│   │   └── 💬 chat_routes.py          # Routes for real-time chat/Q&A
│   ├── 📁 services
│   │   ├── 📝 db_service.py           # MongoDB interaction
│   │   └── 🧠 rag_engine.py           # LangChain + FAISS + OpenRouter.ai integration
│   ├── ⚙️ config.py                   # Config handling (env loading)
│   └── 📦 requirements.txt            # Python dependencies
│
├── 📁 node-server                     # WebSocket bridge
│   └── 📝 server.js                   # Node.js WebSocket server
│
├── 📁 frontend                        # React frontend
│   ├── 📁 public
│   │   └── 📝 index.html              # HTML template
│   ├── 📁 src
│   │   ├── 📁 components
│   │   │   ├── 🧑 Register.js         # Face Registration UI
│   │   │   ├── 👁️ LiveRecognition.js # Live face recognition UI
│   │   │   └── 💬 ChatWidget.js      # Chat interface for Q&A
│   │   ├── 🧩 App.js                 # Main app layout
│   │   └── 📍 index.js               # React entry point
│   └── 📦 package.json               # Frontend dependencies
│
├── 🔐 .env                            # API keys and Mongo URI (excluded from version control)
├── 📘 README.md                       # Project documentation
└── 🖼️ architecture.png               # System architecture diagram

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
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=google/gemma-7b-it

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
| AI Engine | LangChain + FAISS + OpenRouter.ai (GPT)   |
| Database  | MongoDB Atlas                             |
| Realtime  | Node.js WebSocket                         |
| DevOps    | GitHub, GitHub Student Pack (API credits) |


💡 RAG Engine

📌 Embeds documents using OpenAIEmbeddings or compatible interface

📁 Stores vectors in FAISS

🧠 Uses LangChain RetrievalQA for question answering

🛰️ Powered by OpenRouter.ai GPT models (like GPT-4, Claude, etc.)


🧠 How It Works
    -📸 Face captured via webcam

    -🔐 Face embeddings stored/retrieved from MongoDB

    -❓ User asks a question

    -🔍 RAG retrieves documents using FAISS

    -🧠 Azure OpenAI generates response

    -💬 Real-time WebSocket sends back answer


Get daily free tokens using:

👉 https://openrouter.ai

## 🖼️ System Architecture

![Architecture Diagram](architecture.png)

---
