import React, { useState } from "react";

const App = () => {
  const [text, setText] = useState("");
  const [data, setData] = useState("");
  const [error, setError] = useState("");



    const fetchData = async () => {
      try {
      const body = JSON.stringify({texts: [ {text: text} ]})
      // const modelapi_service = `http://${process.env.MODELAPI_SERVICE_ADDRESS}:${process.env.MODELAPI_SERVICE_PORT}/predict`
      // const modelapi_service = 'http://modelapi-service.default:8000/predict'
      const modelapi_service = 'http://a4bab88ce3ecc4d49987983c22eb6317-1386881726.ap-south-1.elb.amazonaws.com:8000/predict'
      console.log(modelapi_service)
      const response = await fetch(modelapi_service,{body: body,method: "POST",headers: {"Content-Type": "application/json"}})
      const data = await response.json();
      console.log(data);
      setData(data);
      setError("");
    } catch (error) {
      setError(error.message);
    };
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
          {data && <h3>The tweet reflects {data.data.prediction[0]}</h3>}
        </>
      )}
    </div>
  );
};

export default App;
