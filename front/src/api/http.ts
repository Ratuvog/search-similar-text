import CONFIG from '../config';
import axios from 'axios';

const http = axios.create({
  baseURL: CONFIG.baseUrl,
  headers: {},
});

export default http;
