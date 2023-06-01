import React, { useState } from "react";

const App = () => {
  const [text, setText] = useState("");
  const [data, setData] = useState("");
  const [error, setError] = useState("");



    const fetchData = async () => {
      let start = new Date().getTime();
      try {
      const body = JSON.stringify({texts: [ {text: text} ]})
      const modelapi_service = 'http://localhost:8000/predict'
      console.log(modelapi_service)
      const response = await fetch(modelapi_service,{body: body,method: "POST",headers: {"Content-Type": "application/json"}})
      const data = await response.json();
      console.log(data);
      setData(data);
      setError("");
    } catch (error) {
      setError(error.message);
    };
    let end = new Date().getTime();
    let time = end - start;
    console.log('Execution time: ' + time); // unit of time here is ms, divide by 1000 to get seconds
  };

  return (
    <div>
      <h1>Find Sentiment of your SocialMedia Posts!</h1>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={(fetchData)}>Analyze Sentiment</button>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <h2>RESULT:</h2>
      {error ? (
        <h3>{error}</h3>
      ) : (
        <>
          {data && <h3>The text reflects {data.data.prediction[0]}</h3>}
        </>
      )}
    </div>
  );
};

export default App;
