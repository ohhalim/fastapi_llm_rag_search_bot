import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!question.trim()) return;

        setLoading(true);
        try {
            const response = await axios.post('http://localhost:8000/api/chat', {
                question: question
            });
            setAnswer(response.data.answer);
        } catch (error) {
            console.error('Error:', error);
            setAnswer('Sorry, an error occurred. Please try again.');
        }
        setLoading(false);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Google Ads API Assistant</h1>

                <form onSubmit={handleSubmit} className="chat-form">
                    <input
                        type="text"
                        value={question}
                        onChange={(e) => setQuestion(e.target.value)}
                        placeholder="Ask about Google Ads API..."
                        className="question-input"
                    />
                    <button type="submit" disabled={loading}>
                        {loading ? 'Thinking...' : 'Ask'}
                    </button>
                </form>

                {answer && (
                    <div className="answer-box">
                        <h3>Answer:</h3>
                        <p>{answer}</p>
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;

