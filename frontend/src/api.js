import axios from "axios";

const API = axios.create({
    baseURL: process.env.REACT_APP_BACKEND_URL || "http://localhost:8000"
});

export const getSources = () => API.get("/sources/");
export const createSource = (data) => API.post("/sources/", data);
export const updateSource = (id, data) => API.put(`/sources/${id}`, data);
export const deleteSource = (id) => API.delete(`/sources/${id}`);