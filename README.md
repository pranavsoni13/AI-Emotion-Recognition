# 🚀 AI Emotion Recognition System

An end-to-end AI-powered web application that detects human emotions from text input and visualizes emotional trends over time.

---

## 🌟 Features

* 🔍 **Emotion Detection** using Hugging Face transformer model
* ⚡ **FastAPI Backend** for high-performance API handling
* 🎯 **Real-time Prediction** from user input
* 📊 **Emotion Dashboard** with dynamic visualization
* 📈 **Timeline Chart** to track emotional trends
* 🌐 **Deployed Full Stack App** (Frontend + Backend)

---

## 🧠 Tech Stack

### 🔹 Frontend

* React (Vite)
* Chart.js
* Axios

### 🔹 Backend

* FastAPI
* Python
* Hugging Face Inference API

### 🔹 Deployment

* Frontend → Vercel
* Backend → Railway

---

## 🏗️ Project Structure

```
AI-Emotion-Recognition/
│
├── frontend/
│   └── emotion-dashboard/
│       ├── src/
│       │   ├── components/
│       │   ├── services/
│       │   └── App.jsx
│
├── backend/
│   └── app/
│       ├── routes/
│       ├── model/
│       ├── database/
│       └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User enters text in frontend
2. Request sent to FastAPI backend
3. Backend calls Hugging Face API
4. Emotion prediction returned
5. Data stored (for timeline tracking)
6. Frontend visualizes:

   * Dominant emotion
   * Emotion distribution
   * Timeline chart

---

## 🔌 API Endpoints

### 📌 Predict Emotion

```
POST /predict
```

**Request:**

```json
{
  "text": "I am feeling great today!"
}
```

**Response:**

```json
{
  "emotions": {
    "joy": 0.92,
    "sadness": 0.03,
    ...
  }
}
```

---

### 📊 Emotion Timeline

```
GET /analytics/emotion-timeline
```

**Response:**

```json
{
  "timeline": [
    { "date": "Entry 1", "emotion": 3 },
    { "date": "Entry 2", "emotion": 1 }
  ]
}
```

---

## 🔥 Key Learnings

* Handling **real-world API integration**
* Fixing **CORS & deployment issues**
* Managing **frontend-backend communication**
* Debugging **async API failures**
* Working with **transformer-based NLP models**

---

## 🚀 Deployment Links

* 🌐 Frontend: (Vercel Link)
* ⚡ Backend: (Railway Link)

---

## 🧩 Future Improvements

* 📅 Real timestamp-based timeline
* 📊 Advanced analytics dashboard
* 🤖 Custom trained emotion model
* 📱 Mobile responsive UI

---

## 🤝 Contribution

Feel free to fork, improve, and contribute!

---

## 👨‍💻 Author

**Pranav Soni**
AI & Data Science Student

---

## 💬 Final Note

This project was built from scratch with real debugging, real deployment struggles, and real learning.

> Not just a project — this is a full-stack AI system 🚀
