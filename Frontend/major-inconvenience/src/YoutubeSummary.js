import React, { useState } from "react";
import axios from "axios";
import "./YoutubeSummary.css";

const YoutubeSummary = () => {
  const [videoLink, setVideoLink] = useState("");
  const [summary, setSummary] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    console.log(">>>>", videoLink);
    axios
      .post(`http://127.0.0.1:5000/api/youtubesummaryHindi`, {link :videoLink})
      .then(function (response) {
        setSummary(response.data.summary);
        console.log("heheh", response.data.summary);
        // console.log("heheh", response.data);
        setLoading(false);
      })
      .catch(function (error) {
        console.error("Error:", error);
      });
  };

  return (
    <div className="youtube-summary-container">
      <div className="input-container">
        <label htmlFor="videoLink">Enter Video Link: ex : "https://www.youtube.com/watch?v=iHHrr9m0Gqc"</label>
        <input
          type="text"
          id="videoLink"
          value={videoLink}
          onChange={(e) => setVideoLink(e.target.value)}
          placeholder="https://www.youtube.com/watch?v=..."
        />
        <button onClick={handleSubmit} disabled={loading}>
          {loading ? "Loading..." : "Submit"}
        </button>
      </div>
      <div className="summary-container">
        <h3>Summary:</h3>
        <ul>
          {summary.map((point, index) => (
            <li key={index}>{point}</li>
          ))}
        </ul>
        {error && <p className="error">{error}</p>}
      </div>
    </div>
  );
};

export default YoutubeSummary;
