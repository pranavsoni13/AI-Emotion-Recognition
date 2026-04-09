import { useEffect, useState } from "react";
import API from "services/api";
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
      const res = await API.get("/analytics/emotion-timeline");
      setTimeline(res.data.timeline);
    } catch (error) {
      console.error(error);
    }
  };

  const labels = timeline.map(item => item.date);
  const emotions = timeline.map(item => item.emotion);

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Emotion Timeline",
        data: emotions.map((_, i) => i + 1),
        borderColor: "#4CAF50",
        tension: 0.3
      }
    ]
  };

  return <Line data={data} />;
}