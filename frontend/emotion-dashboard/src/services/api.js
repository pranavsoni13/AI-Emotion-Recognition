const BASE_URL ="https://ai-emotion-recognition-production.up.railway.app";

const API = {
  // prediction
  predict: async (text) => {
    try {
      const response = await fetch(`${BASE_URL}/predict`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      return await response.json();
    } catch (error) {
      console.error("API error:", error);
      return { error: "Failed to fetch" };
    }
  },

  // timeline
  timeline: async () => {
    try {
      const response = await fetch(`${BASE_URL}/analytics/emotion-timeline`);
      return await response.json();
    } catch (error) {
      console.error("Timeline error:", error);
      return { timeline: [] };
    }
  },
};

export default API;