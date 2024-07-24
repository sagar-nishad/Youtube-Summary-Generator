import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <div className="button-container">
        <Link to="/summarization" className="button">Summarization</Link>
        <Link to="/ytSummaryhindi" className="button">Youtube Summary Hindi </Link>
        <Link to="/ytSummaryenglish" className="button">Youtube Summary Engish</Link>
    
      </div>
    </div>
  );
};

export default LandingPage;
