import logo from './logo.svg';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import './App.css';
import LandingPage from './LandingPage';
import Summarization from './Summarization';
import YoutubeSummary from './YoutubeSummary';
import DefaultYTSummary from './DefaultYTSummary';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
    <Routes>
    <Route path="/" exact element={<LandingPage />} />
    <Route path="/summarization" exact element={<Summarization />} />
    <Route path="/ytSummaryhindi" exact element={<YoutubeSummary />} />
    <Route path="/ytSummaryenglish" exact element={<DefaultYTSummary />} />

      </Routes>
  </BrowserRouter>
    </div>
  );
}

export default App;
