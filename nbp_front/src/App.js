import React, { useState } from "react";
import "./App.css";
import NbpTabs from "./components/NbpTabs";

function App() {
  const [isProcessing, setIsProcessing] = useState(false);

  return (
    <div className="App">
      <NbpTabs setIsProcessing={true}/>
    </div>
  );
}

export default App;
