import { useState, useEffect } from "react";
import TimelineChart from "./components/TimelineChart";
import EmotionInput from "./components/EmotionInput";
import EmotionChart from "./components/EmotionChart";

function App() {
  const [analytics,setAnalytics]=useState(null);

  useEffect(()=>{
 fetch("http://127.0.0.1:8000/analytics")
  .then(res=>res.json())
  .then(data=>setAnalytics(data));
  },[]);

  const [emotionData, setEmotionData] = useState(null);

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>AI Emotion Dashboard</h1>

      <div style={styles.row}>

        <div style={styles.card}>
          <EmotionInput setEmotionData={setEmotionData} />
        </div>

        <div style={styles.card}>
          <h2>Emotion Distribution</h2>

          {emotionData ? (
            <EmotionChart data={emotionData} />
          ) : (
            <p>Enter text to see emotion distribution</p>
          )}

        </div>

      </div>

      <div style={styles.timeline}>
        <h2>Emotion Timeline</h2>
        <TimelineChart />
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "40px",
    fontFamily: "Arial",
    minHeight: "100vh",
    background: "#1f1f1f",
    color: "white"
  },

  title: {
    textAlign: "center",
    marginBottom: "40px"
  },

  row: {
    display: "flex",
    gap: "20px"
  },

  card: {
    flex: 1,
    padding: "25px",
    background: "#2a2a2a",
    borderRadius: "12px"
  },

  timeline: {
    marginTop: "30px",
    padding: "25px",
    background: "#2a2a2a",
    borderRadius: "12px"
  }
};

export default App;