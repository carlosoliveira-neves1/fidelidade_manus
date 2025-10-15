import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || ''
})

export function setToken(token) {
  api.defaults.headers.common['Authorization'] = 'Bearer ' + token
}

api.interceptors.response.use(
  (r) => r,
  (err) => {
    const code = err?.response?.status
    if (code === 401 || code === 422) {
      localStorage.clear()
      if (!location.pathname.includes('/login')) location.href = '/login'
    }
    return Promise.reject(err)
  }
)

export default Object.assign(api, { setToken })