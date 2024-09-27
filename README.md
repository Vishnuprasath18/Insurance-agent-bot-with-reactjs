

---

# AI Insurance Agent Bot with ReactJS

This project is an AI-powered insurance agent bot designed to answer questions about insurance plans using natural language processing. It uses a ReactJS frontend and a Flask backend, integrated with LangChain components and ChromaDB for managing embeddings.

## Features

- **Interactive Chatbot**: The bot provides answers to queries related to insurance plans.
- **Frontend**: Built with ReactJS for an intuitive user interface.
- **Backend**: Powered by Flask and integrated with ChromaDB and LangChain.
- **Local Model**: The chatbot uses the Mistral model running locally for fast response times.
- **Storage**: ChromaDB stores embeddings for document search and retrieval.

## Tech Stack

- **Frontend**: ReactJS
- **Backend**: Flask
- **Database**: ChromaDB for embedding storage
- **Language Model**: Mistral model (local)
- **NLP Framework**: LangChain
- **UI Framework**: ReactJS components for an engaging chat interface

## Prerequisites

- Node.js
- Python 3.x
- Flask
- ChromaDB
- Ollama Mistral model (locally hosted)
- LangChain

## Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Vishnuprasath18/Insurance-agent-bot-with-reactjs.git
   cd Insurance-agent-bot-with-reactjs/backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Run the React development server:
   ```bash
   npm start
   ```

## Usage

- Open the app in your browser at `http://localhost:3000`.
- Start chatting with the AI Insurance Agent to get answers about various insurance plans.

## Folder Structure

```
Insurance-agent-bot-with-reactjs/
│
├── backend/
│   ├── app.py             # Flask backend
│   ├── chromadb/          # ChromaDB storage
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.js         # Main React app file
│   └── ...
│
└── README.md              # Project documentation
```

## License

This project is licensed under the MIT License.

---


