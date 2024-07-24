import React, { useState } from 'react';
import axios from 'axios';
import './Summarization.css';

const Summarization = () => {
  const [inputText, setInputText] = useState('');
  const [resultText, setResultText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    axios
    .get(`http://127.0.0.1:5000/api/summarize?text=${inputText}`)
    .then(function (response) {
      setResultText(response.data.text);
      console.log("heheh",response.data)
     
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
  };

  return (
    <div className="container">
      <div className="input-container">
        <form onSubmit={handleSubmit}>
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Enter text..."
            rows={10}
            cols={50}
          />
          <br />
          <button type="submit">Submit</button>
        </form>
      </div>
      <div className="result-container">
        <textarea
          value={resultText}
          readOnly
          placeholder="Result..."
          rows={10}
          cols={50}
        />
      </div>
    </div>
  );
};

export default Summarization;
