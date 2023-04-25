import React, { useState } from "react";

const App = () => {
  const [text, setText] = useState("");

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
      <button onClick={() => alert(text)}>Analyze Sentiment</button>
    </div>
  );
};

export default App;
