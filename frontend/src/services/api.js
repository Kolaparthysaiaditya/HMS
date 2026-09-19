import axios from "axios";

const API = axios.create({
  baseURL: "https://hms-4z05.onrender.com/api/",
});

export default API;