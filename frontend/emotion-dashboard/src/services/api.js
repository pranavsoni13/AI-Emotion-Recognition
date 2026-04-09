const API_URL=import.meta.env.VITE_API_URL;
const BASE_URL=API_URL || "https://ai-emotion-recognition-production.up.railway.app";

export const API = async (text) => {
  try {
    const response = await fetch(`${BASE_URL}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    return data;

  } catch (error) {
    console.error("API error:", error);
    return { error: "Failed to fetch" };
  }
};