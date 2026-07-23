import { useEffect, useState } from "react";
import api from "./api/api";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    api.get("/")
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Palmistry & Tarot</h1>
      <h2>{message}</h2>
    </div>
  );
}

export default App;