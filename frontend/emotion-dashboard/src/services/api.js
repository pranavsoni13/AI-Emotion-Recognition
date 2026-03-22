import axios from "axios";

const API = axios.create({
  baseURL: "https://emotion-backend-skns.onrender.com",
  timeout: 120000
});

export default API;