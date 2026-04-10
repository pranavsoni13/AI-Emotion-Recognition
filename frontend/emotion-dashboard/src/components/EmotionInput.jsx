import { useState } from "react";
import API from "../services/api";

function EmotionInput({ setEmotionData }) {

  const emotionEmoji = {
    joy: "😄",
    sadness: "😢",
    anger: "😡",
    fear: "😨",
    surprise: "😲",
    neutral: "😐",
    disgust: "🤢"
  };

  const emotionColors = {
    anger: "#ff4d4f",
    fear: "#722ed1",
    joy: "#52c41a",
    love: "#eb2f96",
    neutral: "#8c8c8c",
    sadness: "#1890ff",
    surprise: "#faad14",
    disgust: "#13c2c2"
  };

  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const dominantEmotion = result
    ? Object.entries(result).reduce((a, b) => (a[1] > b[1] ? a : b))
    : null;

  const analyze = async () => {
  console.log("Analyze clicked");

  try {
    const data = await API.predict(text);

    if (!data || data.error) {
      console.error("No data received from API");
      return;
    }

    console.log("API response:", data);

    // 🔥 FIX HERE ONLY
    setResult(data.emotions);
    setEmotionData(data.emotions);

  } catch (error) {
    console.error("API error", error);
  }
};

  return (
    <div>

      <input
        type="text"
        placeholder="Enter text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            analyze();
          }
        }}
      />

      <button onClick={analyze} disabled={!text.trim()}>
        Analyze
      </button>

      {/* ✅ Dominant Emotion */}
      {dominantEmotion && (
        <div className="dominant-card">
          <h3>Dominant Emotion</h3>
          <h2>
            {emotionEmoji[dominantEmotion[0]]}{" "}
            {dominantEmotion[0].toUpperCase()}
          </h2>
          <p>
            Confidence: {(dominantEmotion[1] * 100).toFixed(1)}%
          </p>
        </div>
      )}

      {/* ✅ All Emotion Bars */}
      {result && (
        <div className="emotion-bars">
          {Object.entries(result).map(([emotion, value]) => (
            <div key={emotion} className="emotion-row">
              <span>
                {emotion} ({(value * 100).toFixed(1)}%)
              </span>

              <div className="bar-container">
                <div
                  className="bar"
                  style={{
                    width: `${value * 100}%`,
                    background: emotionColors[emotion] || "#999"
                  }}
                ></div>
              </div>

            </div>
          ))}
        </div>
      )}

    </div>
  );
}

export default EmotionInput;