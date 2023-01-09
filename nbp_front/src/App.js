import React, { useState } from "react";
import "./App.css";
import Exchange from './pages/Exchange';

function App() {
  const [isProcessing, setIsProcessing] = useState(false);

  return (
    <div className="App">
      <Exchange setIsProcessing={true}/>
    </div>
  );
}

export default App;
