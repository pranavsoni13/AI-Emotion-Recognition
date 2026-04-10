import axios from "axios";

const BASE_URL = "https://ai-emotion-recognition-production.up.railway.app";

const API = {
  predict: async (text) => {
    try {
      const response = await axios.post(`${BASE_URL}/predict`, {
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({text:inputText}),
      });
      const data = await response.json();

      return data;
    } catch (error) {
      console.error("API error:", error);
      return null;
    }
  },

  // 🔥 timeline
  timeline: async () => {
    try {
      const response = await axios.get(
        `${BASE_URL}/analytics/emotion-timeline`
      );

      return response.data;
    } catch (error) {
      console.error("Timeline error:", error);
      return { timeline: [] };
    }
  },
};

export default API;