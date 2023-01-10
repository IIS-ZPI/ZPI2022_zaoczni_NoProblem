import React, { useState } from "react";
import "./App.css";
import CurrentRate from './pages/CurrentRate';
import SelectCurrency from './pages/SelectCurrency';

function App() {
  const [isProcessing, setIsProcessing] = useState(false);

  return (
    <div className="App">
      <CurrentRate setIsProcessing={true} currencyCode="USD" />
      <SelectCurrency setIsProcessing={true} />
    </div>
  );
}

export default App;
