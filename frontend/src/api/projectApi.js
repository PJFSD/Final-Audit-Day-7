import axios from "axios";

const API_URL = "http://localhost:8000";

// GET Projects
export const fetchProjects = async () => {
  const res = await axios.get(`${API_URL}/projects`);
  return res.data;
};

// POST Project
export const createProject = async (projectData) => {
  const res = await axios.post(`${API_URL}/projects`, projectData);
  return res.data;
};