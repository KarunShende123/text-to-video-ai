import { useState } from 'react';
import axios from 'axios';

export default function GenerateVideo() {
  const [prompt, setPrompt] = useState("");
  const [status, setStatus] = useState("");

  const handleSubmit = async () => {
    const res = await axios.post("http://localhost:8000/generate-video", { prompt });
    setStatus(`Task submitted: ${res.data.task_id}`);
  };

  return (
    <div className="p-8">
      <input value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="Enter a video prompt" />
      <button onClick={handleSubmit} className="ml-4">Generate</button>
      <p>{status}</p>
    </div>
  );
}
