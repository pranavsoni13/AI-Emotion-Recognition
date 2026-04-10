import { useEffect, useState } from "react";
import API from "../services/api";

import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
);

export default function TimelineChart() {
  const [timeline, setTimeline] = useState([]);

  useEffect(() => {
    fetchTimeline();
  }, []);

  const fetchTimeline = async () => {
    try {
      const res = await API.timeline();
      console.log("Timeline API:", res);

      if (res && res.timeline) {
        setTimeline(res.timeline);
      } else {
        setTimeline([]);
      }

    } catch (error) {
      console.error("Timeline error:", error);
      setTimeline([]);
    }
  };

  // ✅ Emotion number → name (optional but clean UI)
  const emotionMap = {
    1: "Sad",
    2: "Neutral",
    3: "Happy",
    4: "Angry"
  };

  const labels = timeline.map(item => item.date);

  const dataPoints = timeline.map(item => item.emotion);

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Emotion Timeline",
        data: dataPoints,
        borderColor: "#4CAF50",
        backgroundColor: "#4CAF50",
        tension: 0.3,
        pointRadius: 5
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: true
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            const value = context.raw;
            return emotionMap[value] || value;
          }
        }
      }
    },
    scales: {
      y: {
        ticks: {
          callback: function(value) {
            return emotionMap[value] || value;
          }
        }
      }
    }
  };

  return <Line data={data} options={options} />;
}