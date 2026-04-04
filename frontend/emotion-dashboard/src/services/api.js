const API_URL = "https://ai-emotion-recognition-production.up.railway.app";

export const predictEmotion = async (text) => {
  try {
    const response = await fetch(`${API_URL}/predict`, {
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