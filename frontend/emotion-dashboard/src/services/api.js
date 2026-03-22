import axios from "axios";

const API = axios.create({
  baseURL: "https://emotion-backend-skns.onrender.com"
});

export default API;