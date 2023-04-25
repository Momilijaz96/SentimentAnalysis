import React, { useState } from "react";

const App = () => {
  const [text, setText] = useState("");
  const [data, setData] = useState("");
  const [error, setError] = useState("");



    const fetchData = async () => {
      try {
      const response = await fetch("http://127.0.0.1:8000/predict");
      const data = await response.json();
      console.log(data);
      setData(data);
      setError("");
    } catch (error) {
      setError(error.message);
    };
    fetchData();

  };
  return (
    <div>
      <h1>Tweet Sentiment Analysis</h1>
      <h1> using DistilBERT</h1>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        onFocus={() => setText("Enter tweet here...")}
      />
      <button onClick={(fetchData)}>Analyze Sentiment</button>
      <textarea
        value={error ? error : JSON.stringify(data)}
        onChange={(e) => setData(e.target.value)}
      />
    </div>
  );
};

export default App;
