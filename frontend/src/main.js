import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import Landing from './pages/Landing.vue'
import Predict from './pages/Predict.vue'
import Insight from './pages/Insight.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Landing', component: Landing },
    { path: '/predict', name: 'Predict', component: Predict },
    { path: '/insight', name: 'Insight', component: Insight }
  ]
})

const app = createApp(App)
app.use(router)
app.mount('#app')
