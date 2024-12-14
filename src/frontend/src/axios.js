import axios from 'axios';

const instance = axios.create({
  baseURL: '/api', // Adjust to your backend URL
});

export default instance;
