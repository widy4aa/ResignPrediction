// API Configuration
export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

// API Endpoints
export const API_ENDPOINTS = {
  health: `${API_URL}/health`,
  features: `${API_URL}/features`,
  predict: `${API_URL}/predict`,
  results: `${API_URL}/api/results`,
  resultsSummary: `${API_URL}/api/results/summary`,
  visualizationsList: `${API_URL}/api/visualizations/list`,
  visualization: (category, filename) => `${API_URL}/api/visualizations/${category}/${filename}`
}

export default API_URL
