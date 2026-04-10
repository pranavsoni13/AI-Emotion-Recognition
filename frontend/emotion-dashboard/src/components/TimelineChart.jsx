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

      // ✅ FIX: safety + fallback
      if (res && res.timeline) {
        setTimeline(res.timeline);
      } else {
        setTimeline([]); // fallback
      }

    } catch (error) {
      console.error(error);
      setTimeline([]); // safety
    }
  };

  // ✅ SAFE mapping (avoid crash)
  const labels = timeline?.map(item => item.date) || [];
  const dataPoints = timeline?.map(item => item.emotion) || [];

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Emotion Timeline",
        data: dataPoints,
        borderColor: "#4CAF50",
        tension: 0.3
      }
    ]
  };

  return <Line data={data} />;
}