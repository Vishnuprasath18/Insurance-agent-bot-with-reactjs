import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');
  const [conversation, setConversation] = useState([]);

  const handleSend = async () => {
    if (question.trim()) {
      try {
        // Send question to Flask backend (ensure it runs on port 5000)
        const res = await axios.post("http://localhost:5000/ask", { question });
        const botResponse = res.data.response;

        // Update conversation history
        const newConversation = [...conversation, { question, botResponse }];
        setConversation(newConversation);

        setResponse(botResponse);
        setQuestion(''); // Clear input field after sending
      } catch (error) {
        console.error('Error fetching response:', error);
        setResponse('Error fetching response.');
      }
    }
  };

  return (
    <div className="App">
      <h1>Chatbot</h1>
      <div className="chat-box">
        {conversation.map((msg, index) => (
          <div key={index}>
            <p><strong>User:</strong> {msg.question}</p>
            <p><strong>Bot:</strong> {msg.botResponse}</p>
          </div>
        ))}
      </div>

      <input
      
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask me something..."
      />
      <button className='btn' onClick={handleSend}>Send</button>
    </div>
  );
}

export default App;
