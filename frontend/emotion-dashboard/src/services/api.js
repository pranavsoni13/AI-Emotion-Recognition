import axios from "axios";

const API = axios.create({
  baseURL: "https://emotion-backend-skns.onrender.com",
  timeout: 60000
});

export default API;