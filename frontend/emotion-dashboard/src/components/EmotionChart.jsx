import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function EmotionChart({ data }) {

  const chartData = {
    labels: Object.keys(data),
    datasets: [
      {
        label: "Emotion Distribution",
        data: Object.values(data),
        backgroundColor: [
          "#ff6384",
          "#36a2eb",
          "#ffcd56",
          "#4bc0c0",
          "#9966ff",
          "#ff9f40",
          "#8bc34a"
        ]
      }
    ]
  };
  return (
    <div style={{height:"300px"}}>
      <Pie data={chartData} />
    </div>
  );
}

export default EmotionChart;